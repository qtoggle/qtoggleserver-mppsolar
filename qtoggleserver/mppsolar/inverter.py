
import asyncio
import logging

from typing import Any, Dict, List, Optional

from mppsolar import mppUtils
from mppsolar import mppinverter
from qtoggleserver.lib.polled import PolledPeripheral

from .exceptions import MPPSolarTimeout


logger = logging.getLogger(__name__)


class MPPSolarInverter(PolledPeripheral):
    DEFAULT_POLL_INTERVAL = 5
    RETRY_POLL_INTERVAL = 5

    DEFAULT_BAUD = 2400
    TIMEOUT = 10

    logger = logger

    def __init__(
        self,
        *,
        serial_port: str,
        serial_baud: int = DEFAULT_BAUD,
        properties: Optional[List[str]] = None,
        **kwargs
    ) -> None:

        self._mpp_utils = mppUtils(serial_port, serial_baud)
        self._status: Dict[str, List[str]] = {}
        self._device_mode: Optional[str] = None
        self._property_names: Optional[List[str]] = properties

        super().__init__(**kwargs)

    def read_status(self) -> None:
        self._status = self._mpp_utils.getResponseDict('QPIGS')
        response = self._mpp_utils.getResponseDict('QMOD')
        self._device_mode = response['device_mode'][0].lower().replace(' ', '_')

    async def poll(self) -> None:
        try:
            future = self.run_threaded(self.read_status)
            await asyncio.wait_for(future, timeout=self.TIMEOUT)

        except asyncio.TimeoutError as e:
            raise MPPSolarTimeout('Timeout waiting for response from inverter') from e

    def get_status_property(self, name: str) -> Optional[List[str]]:
        return self._status.get(name)

    def get_device_mode(self) -> Optional[str]:
        return self._device_mode

    async def make_port_args(self) -> List[Dict[str, Any]]:
        from .ports import BooleanStatusPort, NumberStatusPort, DeviceModePort

        commands = mppinverter.getCommandsFromJson(inverter_model='standard')
        qpigs_cmd = next(c for c in commands if c.name == 'QPIGS')

        port_args = [
            DeviceModePort
        ]

        for _type, display_name, unit in qpigs_cmd.response_definition:
            if _type == 'flags':
                for n in unit:
                    if self._property_names and n not in self._property_names:
                        continue

                    port_args.append({
                        'driver': BooleanStatusPort,
                        'property_name': n,
                        'display_name': n.replace('_', ' ').title()
                    })

            elif _type in ('int', 'float'):
                name = display_name.lower().replace(' ', '_')
                if self._property_names and name not in self._property_names:
                    continue

                port_args.append({
                    'driver': NumberStatusPort,
                    'property_name': name,
                    'display_name': display_name,
                    'unit': unit
                })

        return port_args
