
from typing import List, Type

from .base import Command
from .mchgc import MCHGC
from .mnchgc import MNCHGC_Parallel, MNCHGC_Single
from .muchgc import MUCHGC_Single, MUCHGC_Parallel
from .qmchgcr import QMCHGCR
from .qmuchgcr import QMUCHGCR
from .qmod import QMOD
from .qpigs import QPIGS, QPIGS_LV, QPIGS_GKMK
from .qpigs2 import QPIGS2, QPIGS2_MAX
from .qpiri import QPIRI, QPIRI_GKMK, QPIRI_MAX


COMMANDS_BY_MODEL = {
    'GK': [
        MNCHGC_Single,
        MUCHGC_Single,
        QMCHGCR,
        QMUCHGCR,
        QMOD,
        QPIGS_GKMK,
        QPIRI_GKMK,
    ],
    'LV': [
        MNCHGC_Single,
        QMCHGCR,
        QMOD,
        QPIGS_LV,
    ],
    'MAX': [
        MCHGC,
        MNCHGC_Parallel,
        MUCHGC_Parallel,
        QMCHGCR,
        QMUCHGCR,
        QMOD,
        QPIGS,
        QPIGS2_MAX,
        QPIRI_MAX,
    ],
    'MK': [
        MNCHGC_Parallel,
        MUCHGC_Parallel,
        QMCHGCR,
        QMOD,
        QPIGS_GKMK,
        QPIRI_GKMK,
    ],
}


def get_command_classes(model: str) -> List[Type[Command]]:
    return COMMANDS_BY_MODEL.get(model, [])
