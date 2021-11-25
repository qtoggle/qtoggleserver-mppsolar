
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

BATTERY_TYPE_CHOICES = [
    (0, 'AGM'),
    (1, 'Flooded'),
    (2, 'User'),
    (3, 'Pylontech'),
]

OUTPUT_SOURCE_PRIORITY_CHOICES = [
    (0, 'Grid/Solar/Battery'),
    (1, 'Solar/Grid/Battery'),
    (2, 'Solar/Battery/Grid'),
]

CHARGING_SOURCE_PRIORITY_CHOICES = [
    (1, 'Solar Then Grid'),
    (2, 'Solar And Grid'),
    (3, 'Only Solar'),
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
