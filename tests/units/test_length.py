import pytest

from unit_converter.units.length import convert_length, is_length_unit


def test_meter_to_centimeter():
    assert convert_length(1, "meter", "centimeter") == pytest.approx(100)


def test_kilometer_to_mile():
    assert convert_length(1, "kilometer", "mile") == pytest.approx(0.621371, abs=5e-6)


def test_foot_to_centimeter():
    assert convert_length(20, "foot", "centimeter") == pytest.approx(609.6, abs=0.5)


def test_inch_to_itself():
    assert convert_length(42, "inch", "inch") == pytest.approx(42)


def test_yard_to_millimeter_zero():
    assert convert_length(0, "yard", "millimeter") == 0


def test_is_length_unit_accepts_known():
    assert is_length_unit("meter") is True


def test_is_length_unit_rejects_unknown():
    assert is_length_unit("lightyear") is False
