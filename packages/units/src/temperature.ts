export const TEMPERATURE_UNITS = ["celsius", "fahrenheit", "kelvin"] as const;

export type TemperatureUnit = (typeof TEMPERATURE_UNITS)[number];

function toCelsius(value: number, from: TemperatureUnit): number {
  switch (from) {
    case "celsius":
      return value;
    case "fahrenheit":
      return (value - 32) * (5 / 9);
    case "kelvin":
      return value - 273.15;
  }
}

function fromCelsius(celsius: number, to: TemperatureUnit): number {
  switch (to) {
    case "celsius":
      return celsius
    case "fahrenheit":
      return celsius * (9 / 5) + 32
    case "kelvin":
      return celsius + 273.15
  }
}

export function isTemperatureUnit(value: string): value is TemperatureUnit {
  return (TEMPERATURE_UNITS as readonly string[]).includes(value);
}

export function convertTemperature(
  value: number,
  from: TemperatureUnit,
  to: TemperatureUnit,
): number {
  return fromCelsius(toCelsius(value, from), to);
}
