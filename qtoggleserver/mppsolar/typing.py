from typing import Any, TypeAlias, Union


Property: TypeAlias = Union[str, int, float, bool]
Properties: TypeAlias = dict[str, Property]
PropertyDefinition: TypeAlias = dict[str, dict[str, Any]]
PropertyDefinitions: TypeAlias = dict[str, PropertyDefinition]
