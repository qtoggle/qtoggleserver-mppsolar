
import abc

from typing import cast

from qtoggleserver.core.typing import NullablePortValue
from qtoggleserver.lib.polled import PolledPort

from .inverter import MPPSolarInverter


class MPPSolarPort(PolledPort, metaclass=abc.ABCMeta):
    def get_peripheral(self) -> MPPSolarInverter:
        return cast(MPPSolarInverter, super().get_peripheral())


class StatusPort(MPPSolarPort):
    def __init__(self, *, property_name: str, display_name: str, **kwargs) -> None:
        self._property_name: str = property_name

        super().__init__(**kwargs)

        self._display_name: str = display_name

    def make_id(self) -> str:
        return self._property_name


class BooleanStatusPort(StatusPort):
    TYPE = 'boolean'

    async def read_value(self) -> NullablePortValue:
        prop = self.get_peripheral().get_status_property(self._property_name)
        if prop:
            return bool(prop[0])


class NumberStatusPort(StatusPort):
    TYPE = 'number'

    def __init__(self, *, unit: str, **kwargs) -> None:
        super().__init__(**kwargs)

        self._unit: str = unit

    async def read_value(self) -> NullablePortValue:
        prop = self.get_peripheral().get_status_property(self._property_name)
        if prop:
            return float(prop[0])
