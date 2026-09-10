from .linear import LinearUnitCategory

WEIGHT_UNITS: tuple[str, ...] = ("milligram", "gram", "kilogram", "ounce", "pound")

# How many grams equal 1 unit.
GRAMS_PER_UNIT: dict[str, float] = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.349523125,
    "pound": 453.59237,
}

_CATEGORY = LinearUnitCategory(WEIGHT_UNITS, GRAMS_PER_UNIT)


def is_weight_unit(value: str) -> bool:
    return _CATEGORY.is_unit(value)


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    return _CATEGORY.convert(value, from_unit, to_unit)
