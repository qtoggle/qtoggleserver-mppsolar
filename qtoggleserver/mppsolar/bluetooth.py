
import abc
import logging
import struct

from typing import Any, Dict, List

from qtoggleserver.lib import ble

from . import constants
from . import ports as mppsolarports
from .inverter import MPPSolarInverter

logger = logging.getLogger(__name__)


class BluetoothStatusPort(ble.BLEPort, metaclass=abc.ABCMeta):
    READ_INTERVAL_MAX = 86400
    READ_INTERVAL_STEP = 1
    READ_INTERVAL_MULTIPLIER = 1


class BooleanStatusPort(mppsolarports.StatusPort, BluetoothStatusPort):
    pass


class NumberStatusPort(mppsolarports.NumberStatusPort, BluetoothStatusPort):
    pass


class StringStatusPort(mppsolarports.StringStatusPort, BluetoothStatusPort):
    pass


class BluetoothMPPSolarInverter(MPPSolarInverter, ble.BLEPeripheral):
    STATUS1_HANDLE = 0x001D
    STATUS2_HANDLE = 0x0020
    PV1_STATUS_HANDLE = 0x0042

    logger = logger

    async def read_status(self) -> None:
        data = await self.read(self.STATUS1_HANDLE)
        self.parse_status1_data(data)

        data = await self.read(self.STATUS2_HANDLE)
        self.parse_status2_data(data)

        data = await self.read(self.PV1_STATUS_HANDLE)
        self.parse_pv1_status_data(data)

    def parse_status1_data(self, data: bytes) -> None:
        (
            ac_input_voltage, ac_input_frequency, ac_output_voltage, ac_output_frequency,
            ac_output_apparent_power, ac_output_active_power, ac_output_load,
            bus_voltage, battery_voltage, battery_charging_current
        ) = struct.unpack('<HHHHHHHHHH', data)

        self._status['ac_input_voltage'] = ac_input_voltage / 10
        self._status['ac_input_frequency'] = ac_input_frequency / 10
        self._status['ac_output_voltage'] = ac_output_voltage / 10
        self._status['ac_output_frequency'] = ac_output_frequency / 10
        self._status['ac_output_apparent_power'] = ac_output_apparent_power
        self._status['ac_output_active_power'] = ac_output_active_power
        self._status['ac_output_load'] = ac_output_load
        self._status['bus_voltage'] = bus_voltage
        self._status['battery_voltage'] = battery_voltage / 100
        self._status['battery_charging_current'] = battery_charging_current

    def parse_status2_data(self, data: bytes) -> None:
        battery_soc, heat_sink_temp, _, _, _, _, mode, _, _, _ = struct.unpack('<HHHHHHHHHH', data)

        self._status['battery_state_of_charge'] = battery_soc
        self._status['heat_sink_temperature'] = heat_sink_temp
        self._status['mode'] = chr(mode)

    def parse_pv1_status_data(self, data: bytes) -> None:
        _, _, _, _, _, pv_current, pv_voltage, pv_power, _, _ = struct.unpack('<HHHHHHHHHH', data)

        self._status['pv_current'] = pv_current / 10
        self._status['pv_voltage'] = pv_voltage / 10
        self._status['pv_power'] = pv_power

    async def make_port_args(self) -> List[Dict[str, Any]]:
        return [
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_input_voltage',
                'display_name': 'AC Input Voltage',
                'unit': 'V'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_input_frequency',
                'display_name': 'AC Input Frequency',
                'unit': 'Hz'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_output_voltage',
                'display_name': 'AC Output Voltage',
                'unit': 'V'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_output_frequency',
                'display_name': 'AC Output Frequency',
                'unit': 'Hz'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_output_apparent_power',
                'display_name': 'AC Output Apparent Power',
                'unit': 'VA'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_output_active_power',
                'display_name': 'AC Output Active Power',
                'unit': 'W'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'ac_output_load',
                'display_name': 'AC Output Load',
                'unit': '%'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'battery_voltage',
                'display_name': 'Battery Voltage',
                'unit': 'V'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'battery_charging_current',
                'display_name': 'Battery Charging Current',
                'unit': 'A'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'battery_state_of_charge',
                'display_name': 'Battery State Of Charge',
                'unit': '%'
            },
            {
                'driver': NumberStatusPort,
                'property_name': 'heat_sink_temperature',
                'display_name': 'Heat Sink Temperature',
                'unit': 'C'
            },
            {
                'driver': StringStatusPort,
                'property_name': 'mode',
                'display_name': 'Inverter Mode',
                'choices': [{'value': c[0], 'display_name': c[1]} for c in constants.MODE_CHOICES]
            }
        ]
