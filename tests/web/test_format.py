from unit_converter.web.format import capitalize, format_number


def test_format_number_strips_trailing_zeros():
    assert format_number(609.60000000000002) == "609.6"


def test_format_number_rounds_to_four_decimals():
    assert format_number(1 / 3) == "0.3333"


def test_format_number_negative_zero_normalizes_to_zero():
    assert format_number(-0.00001) == "0"


def test_capitalize():
    assert capitalize("kilometer") == "Kilometer"
