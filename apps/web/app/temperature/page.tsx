import { TEMPERATURE_UNITS, type TemperatureUnit } from "@repo/units";
import { ConversionForm } from "@/components/ConversionForm";
import { ResultCard } from "@/components/ResultCard";
import { formatNumber } from "@/lib/format";
import { convertTemperatureAction } from "./actions";

// Celsius and Fahrenheit are conventionally shown with a degree symbol;
// Kelvin is not ("K", never "°K"), so plain capitalize() would be misleading here.
const TEMPERATURE_LABELS: Record<TemperatureUnit, string> = {
  celsius: "Celsius (°C)",
  fahrenheit: "Fahrenheit (°F)",
  kelvin: "Kelvin (K)",
};

const UNIT_OPTIONS = TEMPERATURE_UNITS.map((unit) => ({
  value: unit,
  label: TEMPERATURE_LABELS[unit],
}));

type TemperaturePageProps = {
  searchParams: Promise<{
    value?: string;
    from?: string;
    to?: string;
    result?: string;
    error?: string;
  }>;
};

export default async function TemperaturePage({ searchParams }: TemperaturePageProps) {
  const params = await searchParams;

  if (params.result) {
    const summary = `${params.value} ${params.from} = ${formatNumber(Number(params.result))} ${params.to}`;
    return <ResultCard summary={summary} resetHref="/temperature" />;
  }

  return (
    <>
      {params.error ? <p className="error">{params.error}</p> : null}
      <ConversionForm
        action={convertTemperatureAction}
        fieldLabel="Enter the temperature to convert"
        units={UNIT_OPTIONS}
      />
    </>
  );
}
