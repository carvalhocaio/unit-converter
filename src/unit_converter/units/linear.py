from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class LinearUnitCategory:
    """A unit category convertible via a single multiplicative factor per unit."""

    units: tuple[str, ...]
    base_factor: Mapping[str, float]

    def is_unit(self, value: str) -> bool:
        return value in self.units

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        base_value = value * self.base_factor[from_unit]
        return base_value / self.base_factor[to_unit]
