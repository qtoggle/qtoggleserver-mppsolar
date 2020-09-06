
import abc
import asyncio
import logging

from typing import Dict, Optional

from qtoggleserver.lib.polled import PolledPeripheral

from .exceptions import MPPSolarTimeout
from .typing import Property


logger = logging.getLogger(__name__)


class MPPSolarInverter(PolledPeripheral, metaclass=abc.ABCMeta):
    DEFAULT_POLL_INTERVAL = 5
    RETRY_POLL_INTERVAL = 5

    DEFAULT_MODEL = 'default'
    TIMEOUT = 10

    logger = logger

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        **kwargs
    ) -> None:

        self._model: str = model
        self._status: Dict[str, Property] = {}

        super().__init__(**kwargs)

    async def read_status(self) -> None:
        raise NotImplementedError

    async def poll(self) -> None:
        try:
            await self.read_status()

        except asyncio.TimeoutError as e:
            raise MPPSolarTimeout('Timeout reading inverter status') from e

    def get_status_property(self, name: str) -> Optional[Property]:
        return self._status.get(name)
