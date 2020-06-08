
from typing import Dict, Optional, Type

from .base import Command
from .qmod import QMOD
from .qpigs import QPIGS, QPIGS_LV, QPIGS_GKMK


DEFAULT_COMMANDS = {
    'QMOD': QMOD,
    'QPIGS': QPIGS
}

COMMANDS_BY_MODEL = {
    'GK': {
        'QPIGS': QPIGS_GKMK
    },
    'LV': {
        'QPIGS': QPIGS_LV
    },
    'MK': {
        'QPIGS': QPIGS_GKMK
    }
}


def get_command_classes(model: str) -> Dict[str, Type[Command]]:
    commands = dict(DEFAULT_COMMANDS)
    commands.update(COMMANDS_BY_MODEL.get(model, {}))

    return commands


def make_command(name: str, model: str, **params) -> Optional[Command]:
    command_class = get_command_classes(model).get(name)
    return command_class(**params)
