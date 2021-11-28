
MODE_POWER_ON = 'P'
MODE_STANDBY = 'S'
MODE_GRID = 'L'
MODE_BATTERY = 'B'
MODE_FAULT = 'F'
MODE_POWER_SAVING = 'H'
MODE_SHUTDOWN = 'D'
MODE_CHARGING = 'C'
MODE_BYPASS = 'Y'
MODE_ECO = 'E'

MODE_CHOICES = [
    (MODE_POWER_ON, 'Power On'),
    (MODE_STANDBY, 'Standby'),
    (MODE_GRID, 'Grid'),
    (MODE_BATTERY, 'Battery'),
    (MODE_FAULT, 'Fault'),
    (MODE_POWER_SAVING, 'Power Saving'),
    (MODE_SHUTDOWN, 'Shutdown'),
    (MODE_CHARGING, 'Charging'),
    (MODE_BYPASS, 'Bypass'),
    (MODE_ECO, 'Eco')
]

BATTERY_TYPE_AGM = 0
BATTERY_TYPE_FLOODED = 1
BATTERY_TYPE_USER = 2
BATTERY_TYPE_PYLONTECH = 3

BATTERY_TYPE_CHOICES = [
    (BATTERY_TYPE_AGM, 'AGM'),
    (BATTERY_TYPE_FLOODED, 'Flooded'),
    (BATTERY_TYPE_USER, 'User'),
    (BATTERY_TYPE_PYLONTECH, 'Pylontech'),
]

OUTPUT_SOURCE_PRIORITY_GSB = 0
OUTPUT_SOURCE_PRIORITY_SGB = 1
OUTPUT_SOURCE_PRIORITY_SBG = 2

OUTPUT_SOURCE_PRIORITY_CHOICES = [
    (OUTPUT_SOURCE_PRIORITY_GSB, 'Grid/Solar/Battery'),
    (OUTPUT_SOURCE_PRIORITY_SGB, 'Solar/Grid/Battery'),
    (OUTPUT_SOURCE_PRIORITY_SBG, 'Solar/Battery/Grid'),
]

CHARGING_SOURCE_PRIORITY_STG = 1
CHARGING_SOURCE_PRIORITY_SAG = 2
CHARGING_SOURCE_PRIORITY_OS = 3

CHARGING_SOURCE_PRIORITY_CHOICES = [
    (0, 'Only Grid'),
    (CHARGING_SOURCE_PRIORITY_STG, 'Solar Then Grid'),
    (CHARGING_SOURCE_PRIORITY_SAG, 'Solar And Grid'),
    (CHARGING_SOURCE_PRIORITY_OS, 'Only Solar'),
]

BATTERY_MAX_DISCHARGING_CURRENT_CHOICES = [
    (0, 'Disabled'),
    (30, '30'),
    (40, '40'),
    (50, '50'),
    (60, '60'),
    (70, '70'),
    (80, '80'),
    (90, '90'),
    (100, '100'),
    (110, '110'),
    (120, '120'),
    (130, '130'),
    (140, '140'),
    (150, '150'),
]

BATTERY_BACK_TO_GRID_VOLTAGE_CHOICES_48V = [
    (44, '44'),
    (45, '45'),
    (46, '46'),
    (47, '47'),
    (48, '48'),
    (49, '49'),
    (50, '50'),
    (51, '51'),
]

BATTERY_BACK_TO_DISCHARGING_VOLTAGE_CHOICES_48V = [
    (48, '48'),
    (49, '49'),
    (50, '50'),
    (51, '51'),
    (52, '52'),
    (53, '53'),
    (54, '54'),
    (55, '55'),
    (56, '56'),
    (57, '57'),
    (58, '58'),
    (0, 'Full'),
]
