import abc
import logging

from qtoggleserver.lib.polled import PolledPeripheral

from .exceptions import MPPSolarTimeout
from .typing import Property


class MPPSolarInverter(PolledPeripheral, metaclass=abc.ABCMeta):
    DEFAULT_POLL_INTERVAL = 5
    DEFAULT_RETRY_POLL_INTERVAL = 5
    DEFAULT_RETRY_COUNT = 2

    TIMEOUT = 10

    logger = logging.getLogger(__name__)

    def __init__(self, *, model: str, **kwargs) -> None:
        self._model: str = model
        self._properties: dict[str, Property] = {}

        super().__init__(**kwargs)

    async def read_properties(self) -> None:
        raise NotImplementedError

    async def poll(self) -> None:
        try:
            await self.read_properties()
        except TimeoutError as e:
            raise MPPSolarTimeout("Timeout reading inverter status") from e

    def get_property(self, name: str) -> Property | None:
        return self._properties.get(name)

    async def set_property(self, name: str, value: Property) -> None:
        raise NotImplementedError
