
import contextlib
import logging
import re

from typing import Any, Dict, List, Optional, Set, Type

from qtoggleserver.utils import json as json_utils

from . import commands
from .io import BaseIO, HIDRawIO, SerialIO
from .inverter import MPPSolarInverter
from .ports import BooleanPort, NumberPort, StringPort
from .typing import Properties, Property


logger = logging.getLogger(__name__)


class SerialMPPSolarInverter(MPPSolarInverter):
    DEFAULT_BAUD = 2400

    # Filter out properties that we don't really want exposed
    BLACKLISTED_PROPERTIES = {
        'has_sbu_priority',
        'is_configuration_status_changed',
        'is_scc_firmware_updated',
        'is_battery_voltage_too_steady_while_charging',
        'battery_voltage_offset_fans',
        'eeprom_version',
        'is_dustproof_installed'
    }

    logger = logger

    def __init__(
        self,
        *,
        serial_port: str,
        serial_baud: int = DEFAULT_BAUD,
        blacklist_properties: Optional[List[str]] = None,
        **kwargs
    ) -> None:

        self._serial_port: str = serial_port
        self._serial_baud: int = serial_baud
        self._blacklist_properties: Set[str] = set(blacklist_properties or [])
        self._setter_command_classes_by_property: Dict[str, List[Type[commands.Command]]] = {}

        super().__init__(**kwargs)

        for cls in commands.get_command_classes(self._model):
            for name in cls.get_request_property_definitions():
                self._setter_command_classes_by_property.setdefault(name, []).append(cls)

    def make_io(self) -> BaseIO:
        if re.match(r'.*hidraw\d+', self._serial_port):
            return HIDRawIO(self._serial_port)
        else:
            return SerialIO(self._serial_port, self._serial_baud)

    async def run_command(self, io: BaseIO, cls: Type[commands.Command], **params) -> Properties:
        params = dict(params, **self.prepare_command_params(cls))
        if params:
            params_str = ', '.join(f'{k}={json_utils.dumps(v)}' for k, v in params.items())
            self.debug('running command %s(%s)', cls.get_name(), params_str)
        else:
            self.debug('running command %s', cls.get_name())

        cmd = cls(**params)
        # Don't run empty commands
        if not cmd.REQUEST_FMT:
            return {}

        request = cmd.prepare_request()
        io.write(request)
        response = await io.read(self.TIMEOUT)
        parsed_response = cmd.parse_response(response)

        return parsed_response

    def prepare_command_params(self, cmd: Type[commands.Command]) -> Properties:
        return cmd.REQUEST_DEFAULT_VALUES

    async def read_properties(self) -> None:
        with contextlib.closing(self.make_io()) as io:
            for cls in commands.get_command_classes(self._model):
                if cls.has_response_properties():
                    self._properties.update(await self.run_command(io, cls))

    async def set_property(self, name: str, value: Property) -> None:
        cmd_classes = self._setter_command_classes_by_property[name]
        params = {name: value}

        with contextlib.closing(self.make_io()) as io:
            for cls in cmd_classes:
                await self.run_command(io, cls, **params)

    async def make_port_args(self) -> List[Dict[str, Any]]:
        # All available command classes for this inverter model
        cmd_classes = commands.get_command_classes(self._model)

        # Fetch property choices
        choices_by_property = {}
        with contextlib.closing(self.make_io()) as io:
            for cls in cmd_classes:
                response_property_definitions = cls.get_response_property_definitions()
                for name, details in response_property_definitions.items():
                    if not details['is_choices']:
                        continue

                    response = await self.run_command(io, cls)
                    choices_by_property[name] = [
                        {
                            'value': c,
                            'label': str(c)
                        }
                        for c in response[name]
                    ]

        # Create port args
        blacklisted_properties = self.BLACKLISTED_PROPERTIES | self._blacklist_properties
        port_args_list = []
        for cls in cmd_classes:
            response_property_definitions = cls.get_response_property_definitions()
            for name, details in response_property_definitions.items():
                if (name in blacklisted_properties) or details['is_choices']:
                    continue

                type_ = details['type']
                port_args = {
                    'property_name': name,
                    'display_name': details['display_name'],
                    'unit': details['unit'],
                    'choices': details['choices'] or choices_by_property.get(name),
                    'writable': name in self._setter_command_classes_by_property
                }
                if type_ == 'bool':
                    port_args['driver'] = BooleanPort
                elif type_ in ('int', 'float'):
                    port_args['driver'] = NumberPort
                elif type_ == 'str':
                    port_args['driver'] = StringPort
                else:
                    continue

                port_args_list.append(port_args)

        return port_args_list
