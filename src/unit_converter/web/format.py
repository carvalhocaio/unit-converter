def capitalize(text: str) -> str:
    """Capitalizes the first letter of a unit name (e.g. "kilometer" -> "Kilometer")."""
    return text[:1].upper() + text[1:]


def format_number(value: float) -> str:
    """Rounds to 4 decimals and trims trailing zeros (e.g. 609.6000...2 -> "609.6")."""
    text = f"{value:.4f}".rstrip("0").rstrip(".")
    if text in ("", "-0"):
        return "0"
    return text
