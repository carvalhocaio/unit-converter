export const WEIGHT_UNITS = ["milligram", "gram", "kilogram", "ounce", "pound"] as const;

export type WeightUnit = (typeof WEIGHT_UNITS)[number];

// How many grams equal 1 unit
const GRAM_PER_UNIT: Record<WeightUnit, number> = {
  milligram: 0.001,
  gram: 1,
  kilogram: 1000,
  ounce: 28.349523125,
  pound: 453.59237,
};

export function isWeightUnit(value: string): value is WeightUnit {
  return (WEIGHT_UNITS as readonly string[]).includes(value);
}

export function convertWeight(value: number, from: WeightUnit, to: WeightUnit): number {
  const grams = value * GRAM_PER_UNIT[from];
  return grams / GRAM_PER_UNIT[to];
}
