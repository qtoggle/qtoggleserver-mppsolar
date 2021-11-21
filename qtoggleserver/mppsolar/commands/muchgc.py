
from .base import Command


class MUCHGC(Command):
    REQUEST_FMT = 'MUCHGC{battery_max_grid_charging_current:03d}'


class MUCHGC_Single(MUCHGC):
    REQUEST_FMT = 'MUCHGC{battery_max_grid_charging_current:03d}'


class MUCHGC_Parallel(MUCHGC):
    REQUEST_FMT = 'MUCHGC{_parallel_no:d}{battery_max_grid_charging_current:03d}'
    REQUEST_DEFAULT_VALUES = {
        '_parallel_no': 0
    }
