from unit_converter.web.validation import parse_finite_float


def test_parse_finite_float_valid():
    assert parse_finite_float("3.5") == 3.5


def test_parse_finite_float_rejects_non_numeric():
    assert parse_finite_float("abc") is None


def test_parse_finite_float_rejects_infinity():
    assert parse_finite_float("Infinity") is None


def test_parse_finite_float_rejects_nan():
    assert parse_finite_float("NaN") is None
