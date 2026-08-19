import { describe, expect, it } from "vitest";
import { convertTemperature, isTemperatureUnit } from "../temperature";

describe("convertTemperature", () => {
  it("converts celsius to fahrenheit (boiling point)", () => {
    expect(convertTemperature(100, "celsius", "fahrenheit")).toBeCloseTo(212);
  });

  it("converts fahrenheit to celsius (freezing point)", () => {
    expect(convertTemperature(32, "fahrenheit", "celsius")).toBeCloseTo(0);
  });

  it("converts celsius to kelvin (absolute zero)", () => {
    expect(convertTemperature(-273.15, "celsius", "kelvin")).toBeCloseTo(0);
  });

  it("converts kelvin to fahrenheit", () => {
    expect(convertTemperature(0, "kelvin", "fahrenheit")).toBeCloseTo(-459.67, 2);
  });

  it("returns the same value when converting a unit to itself", () => {
    expect(convertTemperature(37, "celsius", "celsius")).toBeCloseTo(37);
  });
});

describe("isTemperatureUnit", () => {
  it("accepts known units", () => {
    expect(isTemperatureUnit("kelvin")).toBe(true);
  });

  it("rejects unknown units", () => {
    expect(isTemperatureUnit("rankine")).toBe(false);
  });
});
