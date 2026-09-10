import pytest

from unit_converter.units.weight import convert_weight, is_weight_unit


def test_kilogram_to_pound():
    assert convert_weight(1, "kilogram", "pound") == pytest.approx(2.20462, abs=5e-5)


def test_ounce_to_gram():
    assert convert_weight(1, "ounce", "gram") == pytest.approx(28.3495, abs=5e-4)


def test_milligram_to_itself():
    assert convert_weight(10, "milligram", "milligram") == pytest.approx(10)


def test_is_weight_unit_accepts_known():
    assert is_weight_unit("pound") is True


def test_is_weight_unit_rejects_unknown():
    assert is_weight_unit("stone") is False
