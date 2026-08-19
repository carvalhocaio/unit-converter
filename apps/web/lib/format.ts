// Capitalizes the first letter of a unit name for display (e.g. "kilometer" -> "Kilometer").
export function capitalize(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

// Rounds a conversion result to a reasonable precision and trims trailing zeros
// (e.g. 609.60000000000002 -> "609.6").
export function formatNumber(value: number): string {
  return Number(value.toFixed(4)).toString();
}
