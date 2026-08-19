import { describe, expect, it } from "vitest";
import { convertLength, isLengthUnit } from "../length";

describe("convertLength", () => {
  it("converts meters to centimeters", () => {
    expect(convertLength(1, "meter", "centimeter")).toBeCloseTo(100);
  });

  it("converts kilometers to miles", () => {
    expect(convertLength(1, "kilometer", "mile")).toBeCloseTo(0.621371, 5);
  });

  it("converts feet to centimeters (matches wireframe example: 20 ft = 609 cm)", () => {
    expect(convertLength(20, "foot", "centimeter")).toBeCloseTo(609.6, 0);
  });

  it("returns the same value when converting a unit to itself", () => {
    expect(convertLength(42, "inch", "inch")).toBeCloseTo(42);
  });

  it("handles zero", () => {
    expect(convertLength(0, "yard", "millimeter")).toBe(0);
  });
});

describe("isLengthUnit", () => {
  it("accepts known units", () => {
    expect(isLengthUnit("meter")).toBe(true);
  });

  it("rejects unknown units", () => {
    expect(isLengthUnit("lightyear")).toBe(false);
  });
});
