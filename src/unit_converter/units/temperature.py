TEMPERATURE_UNITS: tuple[str, ...] = ("celsius", "fahrenheit", "kelvin")


def _to_celsius(value: float, from_unit: str) -> float:
    if from_unit == "celsius":
        return value
    if from_unit == "fahrenheit":
        return (value - 32) * (5 / 9)
    if from_unit == "kelvin":
        return value - 273.15
    raise ValueError(f"Unknown temperature unit: {from_unit!r}")


def _from_celsius(celsius: float, to_unit: str) -> float:
    if to_unit == "celsius":
        return celsius
    if to_unit == "fahrenheit":
        return celsius * (9 / 5) + 32
    if to_unit == "kelvin":
        return celsius + 273.15
    raise ValueError(f"Unknown temperature unit: {to_unit!r}")


def is_temperature_unit(value: str) -> bool:
    return value in TEMPERATURE_UNITS


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    return _from_celsius(_to_celsius(value, from_unit), to_unit)
