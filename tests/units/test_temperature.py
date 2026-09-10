import pytest

from unit_converter.units.temperature import convert_temperature, is_temperature_unit


def test_celsius_to_fahrenheit_boiling():
    assert convert_temperature(100, "celsius", "fahrenheit") == pytest.approx(212)


def test_fahrenheit_to_celsius_freezing():
    assert convert_temperature(32, "fahrenheit", "celsius") == pytest.approx(0)


def test_celsius_to_kelvin_absolute_zero():
    assert convert_temperature(-273.15, "celsius", "kelvin") == pytest.approx(0)


def test_kelvin_to_fahrenheit():
    assert convert_temperature(0, "kelvin", "fahrenheit") == pytest.approx(
        -459.67, abs=5e-3
    )


def test_celsius_to_itself():
    assert convert_temperature(37, "celsius", "celsius") == pytest.approx(37)


def test_is_temperature_unit_accepts_known():
    assert is_temperature_unit("kelvin") is True


def test_is_temperature_unit_rejects_unknown():
    assert is_temperature_unit("rankine") is False
