
from .base import Command


class QPIGS(Command):
    REQUEST_FMT = 'QPIGS'

    RESPONSE_FMT = (
        '{ac_input_voltage:f} '
        '{ac_input_frequency:f} '
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
        '{is_battery_charging_from_ac_input:b}'
    )

    UNITS = {
        'ac_input_voltage': 'V',
        'ac_input_frequency': 'Hz',
        'ac_output_voltage': 'V',
        'ac_output_frequency': 'Hz',
        'ac_output_apparent_power': 'VA',
        'ac_output_active_power': 'W',
        'ac_output_load': '%',
        'bus_voltage': 'V',
        'battery_voltage': 'V',
        'battery_charging_current': 'A',
        'battery_state_of_charge': '%',
        'heat_sink_temperature': 'C',
        'pv_current': 'A',
        'pv_voltage': 'V',
        'scc_voltage': 'V',
        'battery_discharging_current': 'A',
        'pv_power': 'W'
    }

    DISPLAY_NAMES = {
        'ac_input_voltage': 'AC Input Voltage',
        'ac_input_frequency': 'AC Input Frequency',
        'ac_output_voltage': 'AC Output Voltage',
        'ac_output_frequency': 'AC Output Frequency',
        'ac_output_apparent_power': 'AC Output Apparent Power',
        'ac_output_active_power': 'AC Output Active Power',
        'ac_output_load': 'AC Output Load',
        'bus_voltage': 'Bus Voltage',
        'battery_voltage': 'Battery Voltage',
        'battery_charging_current': 'Battery Charging Current',
        'battery_state_of_charge': 'Battery State Of Charge',
        'heat_sink_temperature': 'Heat Sink Temperature',
        'pv_current': 'PV Current',
        'pv_voltage': 'PV Voltage',
        'scc_voltage': 'SCC Voltage',
        'battery_discharging_current': 'Battery Discharging Current',
        'has_sbu_priority': 'Has SBU Priority',
        'is_configuration_status_changed': 'Configuration Status Changed',
        'is_scc_firmware_updated': 'SCC Firmware Updated',
        'has_load': 'Has Load',
        'is_battery_voltage_too_steady_while_charging': 'Battery Voltage Too Steady While Charging',
        'is_battery_charging': 'Battery Charging',
        'is_battery_charging_from_scc': 'Battery Charging From SCC',
        'is_battery_charging_from_ac_input': 'Battery Charging From AC Input',
        'pv_power': 'PV Power'
    }

    VIRTUAL_PROPERTIES = {
        'pv_power': {
            'value': lambda properties: properties.get('pv_current', 0) * properties.get('pv_voltage', 0),
            'type': 'float'
        }
    }


class QPIGS_LV(QPIGS):
    RESPONSE_FMT = (
        '{ac_input_voltage:f} '
        '{ac_input_frequency:f} '
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
        '{is_battery_charging_from_ac_input:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_low:b}'
        '{is_battery_present:b}'
        '{is_ac_input_present:b}'
        '{has_load:b} '
        '{_reserved_1:s} '
        '{_reserved_2:s} '
        '{pv_power:f} '
        '{is_battery_float_charging:b}'
        '{is_turned_on:b}'
        '{_reserved_3:b}'
    )

    VIRTUAL_PROPERTIES = {
        'is_battery_charging': {
            'value': lambda properties: (
                properties.get('is_battery_charging_from_ac_input', False) or
                properties.get('is_battery_charging_from_scc', False)
            ),
            'type': 'bool'
        }
    }

    DISPLAY_NAMES = dict(QPIGS.DISPLAY_NAMES, **{
        'is_scc_active': 'SCC Active',
        'is_battery_low': 'Battery Low',
        'is_battery_present': 'Battery Present',
        'is_ac_input_present': 'AC Input Present',
        'pv_power': 'PV Power',
        'is_battery_float_charging': 'Battery Float-charging',
        'is_turned_on': 'Turned On',
    })


class QPIGS_GKMK(QPIGS):
    RESPONSE_FMT = (
        '{ac_input_voltage:f} '
        '{ac_input_frequency:f} '
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
        '{is_ac_output_from_ac_input_or_pv:b}'
        '{is_configuration_status_changed:b}'
        '{is_scc_firmware_updated:b}'
        '{has_load:b}'
        '{_reserved_1:b}'
        '{is_battery_charging:b}'
        '{is_battery_charging_from_scc:b}'
        '{is_battery_charging_from_ac_input:b} '
        '{battery_voltage_offset_fans:f} '
        '{eeprom_version:d} '
        '{pv_power:f} '
        '{is_battery_float_charging:b}'
        '{is_turned_on:b}'
        '{is_dustproof_installed:b}'
    )

    UNITS = dict(QPIGS.UNITS, **{
        'battery_voltage_offset_fans': '10mV'
    })

    DISPLAY_NAMES = dict(QPIGS.DISPLAY_NAMES, **{
        'is_ac_output_from_ac_input_or_pv': 'AC Output From AC Input/PV',
        'battery_voltage_offset_fans': 'Battery Voltage Offset Fans',
        'eeprom_version': 'EEPROM Version',
        'is_battery_float_charging': 'Battery Float-charging',
        'is_turned_on': 'Turned On',
        'is_dustproof_installed': 'Dustproof Installed'
    })
