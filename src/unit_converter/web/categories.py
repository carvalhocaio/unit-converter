from collections.abc import Callable
from dataclasses import dataclass

from unit_converter.units import (
    LENGTH_UNITS,
    TEMPERATURE_UNITS,
    WEIGHT_UNITS,
    convert_length,
    convert_temperature,
    convert_weight,
    is_length_unit,
    is_temperature_unit,
    is_weight_unit,
)

from .format import capitalize


@dataclass(frozen=True)
class UnitOption:
    value: str
    label: str


@dataclass(frozen=True)
class ConversionCategory:
    slug: str
    nav_label: str
    field_label: str
    units: tuple[UnitOption, ...]
    default_to_value: str
    is_unit: Callable[[str], bool]
    convert: Callable[[float, str, str], float]


LENGTH_CATEGORY = ConversionCategory(
    slug="length",
    nav_label="Length",
    field_label="Enter the length to convert",
    units=tuple(UnitOption(unit, capitalize(unit)) for unit in LENGTH_UNITS),
    default_to_value=LENGTH_UNITS[1],
    is_unit=is_length_unit,
    convert=convert_length,
)

WEIGHT_CATEGORY = ConversionCategory(
    slug="weight",
    nav_label="Weight",
    field_label="Enter the weight to convert",
    units=tuple(UnitOption(unit, capitalize(unit)) for unit in WEIGHT_UNITS),
    default_to_value=WEIGHT_UNITS[1],
    is_unit=is_weight_unit,
    convert=convert_weight,
)

# Celsius and Fahrenheit are conventionally shown with a degree symbol;
# Kelvin is not ("K", never "°K").
_TEMPERATURE_LABELS = {
    "celsius": "Celsius (°C)",
    "fahrenheit": "Fahrenheit (°F)",
    "kelvin": "Kelvin (K)",
}

TEMPERATURE_CATEGORY = ConversionCategory(
    slug="temperature",
    nav_label="Temperature",
    field_label="Enter the temperature to convert",
    units=tuple(
        UnitOption(unit, _TEMPERATURE_LABELS[unit]) for unit in TEMPERATURE_UNITS
    ),
    default_to_value=TEMPERATURE_UNITS[1],
    is_unit=is_temperature_unit,
    convert=convert_temperature,
)

CATEGORIES: tuple[ConversionCategory, ...] = (
    LENGTH_CATEGORY,
    WEIGHT_CATEGORY,
    TEMPERATURE_CATEGORY,
)
