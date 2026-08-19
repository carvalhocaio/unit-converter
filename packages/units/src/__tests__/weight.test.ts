import { describe, expect, it } from "vitest";
import { convertWeight, isWeightUnit } from "../weight";

describe("convertWeight", () => {
  it("converts kilograms to pounds", () => {
    expect(convertWeight(1, "kilogram", "pound")).toBeCloseTo(2.20462, 4);
  });

  it("converts ounces to grams", () => {
    expect(convertWeight(1, "ounce", "gram")).toBeCloseTo(28.3495, 3);
  });

  it("returns the same value when converting a unit to itself", () => {
    expect(convertWeight(10, "milligram", "milligram")).toBeCloseTo(10);
  });
});

describe("isWeightUnit", () => {
  it("accepts known units", () => {
    expect(isWeightUnit("pound")).toBe(true);
  });

  it("rejects unknown units", () => {
    expect(isWeightUnit("stone")).toBe(false);
  });
});
