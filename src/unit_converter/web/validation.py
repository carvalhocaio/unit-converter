import math


def parse_finite_float(raw: str) -> float | None:
    """Parses a form value as a finite float, mirroring Number.isFinite(Number(x))."""
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) else None
