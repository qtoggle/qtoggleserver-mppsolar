
import logging
import re

from typing import Any, Dict, List, Optional, Set

from qtoggleserver.utils import json as json_utils

from . import commands
from .io import BaseIO, HIDRawIO, SerialIO
from .inverter import MPPSolarInverter
from .ports import BooleanStatusPort, NumberStatusPort, StringStatusPort
from .typing import Properties


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

        super().__init__(**kwargs)

    def make_io(self) -> BaseIO:
        if re.match(r'.*hidraw\d+', self._serial_port):
            return HIDRawIO(self._serial_port)

        else:
            return SerialIO(self._serial_port, self._serial_baud)

    async def run_command(self, io: BaseIO, name: str, **params) -> Properties:
        if params:
            params_str = ', '.join(f'{k}={json_utils.dumps(v)}' for k, v in params.items())
            self.debug('running command %s(%s)', name, params_str)

        else:
            self.debug('running command %s', name)

        cmd = commands.make_command(name, self._model, **params)
        request = cmd.prepare_request()
        io.write(request)
        response = await io.read(self.TIMEOUT)
        parsed_response = cmd.parse_response(response)

        self.debug('got response to command %s', name)

        return parsed_response

    async def read_status(self) -> None:
        io = self.make_io()

        # Read status using QPIGS command
        self._status.update(await self.run_command(io, 'QPIGS'))

        # Read device mode using QMOD command
        self._status.update(await self.run_command(io, 'QMOD'))

        io.close()

    async def make_port_args(self) -> List[Dict[str, Any]]:
        port_args = []

        command_classes = commands.get_command_classes(self._model)
        status_command_classes = []

        qpigs_command = command_classes.get('QPIGS')
        if qpigs_command:
            status_command_classes.append(qpigs_command)

        qmod_command = command_classes.get('QMOD')
        if qmod_command:
            status_command_classes.append(qmod_command)

        for command_class in status_command_classes:
            for name, details in command_class.get_response_property_definitions().items():
                if name in self.BLACKLISTED_PROPERTIES:
                    continue

                if name in self._blacklist_properties:
                    continue

                type_ = details['type']

                if type_ == 'bool':
                    port_args.append({
                        'driver': BooleanStatusPort,
                        'property_name': name,
                        'display_name': details['display_name']
                    })

                elif type_ in ('int', 'float'):
                    port_args.append({
                        'driver': NumberStatusPort,
                        'property_name': name,
                        'display_name': details['display_name'],
                        'unit': details['unit'],
                        'choices': details['choices']
                    })

                elif type_ == 'str':
                    port_args.append({
                        'driver': StringStatusPort,
                        'property_name': name,
                        'display_name': details['display_name'],
                        'unit': details['unit'],
                        'choices': details['choices']
                    })

        return port_args
