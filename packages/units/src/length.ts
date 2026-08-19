export const LENGTH_UNITS = [
  "millimeter",
  "centimeter",
  "meter",
  "kilometer",
  "inch",
  "foot",
  "yard",
  "mile"
] as const;

export type LengthUnit = (typeof LENGTH_UNITS)[number];

// How many meters equal 1 unit
const METERS_PER_UNIT: Record<LengthUnit, number> = {
  millimeter: 0.001,
  centimeter: 0.01,
  meter: 1,
  kilometer: 1000,
  inch: 0.0254,
  foot: 0.3048,
  yard: 0.9144,
  mile: 1609.344,
};

export function isLengthUnit(value: string): value is LengthUnit {
  return (LENGTH_UNITS as readonly string[]).includes(value);
}

export function convertLength(value: number, from: LengthUnit, to: LengthUnit): number {
  const meters = value * METERS_PER_UNIT[from];
  return meters / METERS_PER_UNIT[to];
}
