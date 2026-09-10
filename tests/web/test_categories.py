from unit_converter.web.categories import CATEGORIES, TEMPERATURE_CATEGORY, UnitOption


def test_categories_have_three_entries_in_nav_order():
    assert [category.slug for category in CATEGORIES] == [
        "length",
        "weight",
        "temperature",
    ]


def test_length_category_labels_are_capitalized():
    length_category = CATEGORIES[0]
    assert UnitOption("kilometer", "Kilometer") in length_category.units


def test_temperature_category_uses_custom_labels():
    assert UnitOption("celsius", "Celsius (°C)") in TEMPERATURE_CATEGORY.units
    assert UnitOption("kelvin", "Kelvin (K)") in TEMPERATURE_CATEGORY.units
