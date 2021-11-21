
from .base import Command


class PBCV(Command):
    REQUEST_FMT = 'PBCV{battery_back_to_grid_voltage:04.1f}'
