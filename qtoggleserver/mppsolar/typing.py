from typing import Any, Union


Property = Union[str, int, float, bool]
Properties = dict[str, Property]
PropertyDefinition = dict[str, dict[str, Any]]
PropertyDefinitions = dict[str, PropertyDefinition]
