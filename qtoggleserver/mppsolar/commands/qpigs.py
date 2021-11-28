
from .base import Command


class QPIGS(Command):
    REQUEST_FMT = 'QPIGS'

    RESPONSE_FMT = (
        '{grid_voltage:f} '
        '{grid_frequency:f} '
        '{ac_output_voltage:f} '
        '{ac_output_frequency:f} '
        '{ac_output_apparent_power:f} '
        '{ac_output_active_power:f} '
        '{ac_output_load:f} '
        '{bus_voltage:f} '
        '{battery_voltage:f} '
        '{battery_charging_current:f} '
        '{battery_state_of_charge:f} '
        '{heat_sink_temperature:f} '
        '{pv_current:f} '
        '{pv_voltage:f} '
        '{scc_voltage:f} '
        '{battery_discharging_current:f} '
        '{has_sbu_priority:b}'
        '{is_configuration_status_changed:b}'
        '{is_scc_firmware_updated:b}'
        '{has_load:b}'
        '{is_battery_voltage_too_steady_while_charging:b}'
        '{is_battery_charging:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_charging_from_grid:b}'
    )

    UNITS = {
        'ac_output_active_power': 'W',
        'ac_output_apparent_power': 'VA',
        'ac_output_frequency': 'Hz',
        'ac_output_load': '%',
        'ac_output_voltage': 'V',
        'battery_charging_current': 'A',
        'battery_discharging_current': 'A',
        'battery_state_of_charge': '%',
        'battery_voltage': 'V',
        'battery_voltage_offset_fans': '10mV',
        'bus_voltage': 'V',
        'grid_frequency': 'Hz',
        'grid_voltage': 'V',
        'heat_sink_temperature': 'C',
        'pv_charging_power': 'W',
        'pv_current': 'A',
        'pv_power': 'W',
        'pv_voltage': 'V',
        'scc_voltage': 'V',
    }

    DISPLAY_NAMES = {
        'ac_output_active_power': 'AC Output Active Power',
        'ac_output_apparent_power': 'AC Output Apparent Power',
        'ac_output_frequency': 'AC Output Frequency',
        'ac_output_load': 'AC Output Load',
        'ac_output_voltage': 'AC Output Voltage',
        'battery_charging_current': 'Battery Charging Current',
        'battery_discharging_current': 'Battery Discharging Current',
        'battery_state_of_charge': 'Battery State Of Charge',
        'battery_voltage': 'Battery Voltage',
        'battery_voltage_offset_fans': 'Battery Voltage Offset Fans',
        'bus_voltage': 'Bus Voltage',
        'eeprom_version': 'EEPROM Version',
        'grid_frequency': 'Grid Frequency',
        'grid_voltage': 'Grid Voltage',
        'has_load': 'Has Load',
        'has_sbu_priority': 'Has SBU Priority',
        'heat_sink_temperature': 'Heat Sink Temperature',
        'is_ac_output_from_grid_or_pv': 'AC Output From Grid/PV',
        'is_battery_charging': 'Battery Charging',
        'is_battery_charging_from_grid': 'Battery Charging From Grid',
        'is_battery_charging_from_scc': 'Battery Charging From SCC',
        'is_battery_float_charging': 'Battery Float-charging',
        'is_battery_low': 'Battery Low',
        'is_battery_present': 'Battery Present',
        'is_battery_voltage_too_steady_while_charging': 'Battery Voltage Too Steady While Charging',
        'is_configuration_status_changed': 'Configuration Status Changed',
        'is_dustproof_installed': 'Dustproof Installed',
        'is_grid_present': 'Grid Present',
        'is_scc_active': 'SCC Active',
        'is_scc_firmware_updated': 'SCC Firmware Updated',
        'is_turned_on': 'Turned On',
        'pv_charging_power': 'PV Charging Power',
        'pv_current': 'PV Current',
        'pv_power': 'PV Power',
        'pv_voltage': 'PV Voltage',
        'scc_voltage': 'SCC Voltage',
    }

    VIRTUAL_PROPERTIES = {
        'pv_power': {
            'value': lambda properties: properties.get('pv_current', 0) * properties.get('pv_voltage', 0),
            'type': 'float'
        },
        'is_battery_charging': {
            'value': lambda properties: (
                properties.get('is_battery_charging_from_grid', False) or
                properties.get('is_battery_charging_from_scc', False)
            ),
            'type': 'bool'
        },
    }


class QPIGS_LV(QPIGS):
    RESPONSE_FMT = (
        '{grid_voltage:f} '
        '{grid_frequency:f} '
        '{ac_output_voltage:f} '
        '{ac_output_frequency:f} '
        '{ac_output_apparent_power:f} '
        '{ac_output_active_power:f} '
        '{ac_output_load:f} '
        '{bus_voltage:f} '
        '{battery_voltage:f} '
        '{battery_charging_current:f} '
        '{battery_state_of_charge:f} '
        '{heat_sink_temperature:f} '
        '{pv_current:f} '
        '{pv_voltage:f} '
        '{scc_voltage:f} '
        '{battery_discharging_current:f} '
        '{is_scc_active:b}'
        '{is_battery_charging_from_grid:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_low:b}'
        '{is_battery_present:b}'
        '{is_grid_present:b}'
        '{has_load:b} '
        '{_reserved_1:s} '
        '{_reserved_2:s} '
        '{pv_power:f} '
        '{is_battery_float_charging:b}'
        '{is_turned_on:b}'
        '{_reserved_3:b}'
    )


class QPIGS_GKMK(QPIGS):
    RESPONSE_FMT = (
        '{grid_voltage:f} '
        '{grid_frequency:f} '
        '{ac_output_voltage:f} '
        '{ac_output_frequency:f} '
        '{ac_output_apparent_power:f} '
        '{ac_output_active_power:f} '
        '{ac_output_load:f} '
        '{bus_voltage:f} '
        '{battery_voltage:f} '
        '{battery_charging_current:f} '
        '{battery_state_of_charge:f} '
        '{heat_sink_temperature:f} '
        '{pv_current:f} '
        '{pv_voltage:f} '
        '{scc_voltage:f} '
        '{battery_discharging_current:f} '
        '{is_ac_output_from_grid_or_pv:b}'
        '{is_configuration_status_changed:b}'
        '{is_scc_firmware_updated:b}'
        '{has_load:b}'
        '{_reserved_1:b}'
        '{is_battery_charging:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_charging_from_grid:b} '
        '{battery_voltage_offset_fans:d} '
        '{eeprom_version:d} '
        '{pv_charging_power:d} '
        '{is_battery_float_charging:b}'
        '{is_turned_on:b}'
        '{is_dustproof_installed:b}'
    )


class QPIGS_MAX(QPIGS):
    RESPONSE_FMT = (
        '{grid_voltage:f} '
        '{grid_frequency:f} '
        '{ac_output_voltage:f} '
        '{ac_output_frequency:f} '
        '{ac_output_apparent_power:f} '
        '{ac_output_active_power:f} '
        '{ac_output_load:f} '
        '{bus_voltage:f} '
        '{battery_voltage:f} '
        '{battery_charging_current:f} '
        '{battery_state_of_charge:f} '
        '{heat_sink_temperature:f} '
        '{pv_current:f} '
        '{pv_voltage:f} '
        '{scc_voltage:f} '
        '{battery_discharging_current:f} '
        '{has_sbu_priority:b}'
        '{is_configuration_status_changed:b}'
        '{is_scc_firmware_updated:b}'
        '{has_load:b}'
        '{is_battery_voltage_too_steady_while_charging:b}'
        '{is_battery_charging:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_charging_from_grid:b} '
        '{battery_voltage_offset_fans:d} '
        '{eeprom_version:d} '
        '{pv_charging_power:d} '
        '{is_battery_float_charging:b}'
        '{is_turned_on:b}'
        '{is_dustproof_installed:b}'
    )
