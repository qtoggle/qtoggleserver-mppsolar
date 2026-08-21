from typing import Any


type Property = str | int | float | bool
type Properties = dict[str, Property]
type PropertyDefinition = dict[str, dict[str, Any]]
type PropertyDefinitions = dict[str, PropertyDefinition]
