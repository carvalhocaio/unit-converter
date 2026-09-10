from .linear import LinearUnitCategory

LENGTH_UNITS: tuple[str, ...] = (
    "millimeter",
    "centimeter",
    "meter",
    "kilometer",
    "inch",
    "foot",
    "yard",
    "mile",
)

# How many meters equal 1 unit.
METERS_PER_UNIT: dict[str, float] = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

_CATEGORY = LinearUnitCategory(LENGTH_UNITS, METERS_PER_UNIT)


def is_length_unit(value: str) -> bool:
    return _CATEGORY.is_unit(value)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    return _CATEGORY.convert(value, from_unit, to_unit)
