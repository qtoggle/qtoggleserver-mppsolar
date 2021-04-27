
from .base import Command


class QPIGS2(Command):
    pass


class QPIGS2_MAX(QPIGS2):
    REQUEST_FMT = 'QPIGS2'

    RESPONSE_FMT = (
        '{pv2_current:f} '
        '{pv2_voltage:f} '
        '{scc2_voltage:f} '
    )

    UNITS = {
        'pv2_current': 'A',
        'pv2_voltage': 'V',
        'scc2_voltage': 'V',
        'pv2_power': 'W'
    }

    DISPLAY_NAMES = {
        'pv2_current': 'PV2 Current',
        'pv2_voltage': 'PV2 Voltage',
        'scc2_voltage': 'SCC2 Voltage',
        'pv2_power': 'PV2 Power'
    }

    VIRTUAL_PROPERTIES = {
        'pv2_power': {
            'value': lambda properties: properties.get('pv2_current', 0) * properties.get('pv2_voltage', 0),
            'type': 'float'
        }
    }
