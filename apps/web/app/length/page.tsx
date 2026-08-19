import { LENGTH_UNITS } from "@repo/units";
import { ConversionForm } from "@/components/ConversionForm";
import { ResultCard } from "@/components/ResultCard";
import { capitalize, formatNumber } from "@/lib/format";
import { convertLengthAction } from "./actions";

const UNIT_OPTIONS = LENGTH_UNITS.map((unit) => ({ value: unit, label: capitalize(unit) }));

type LengthPageProps = {
  searchParams: Promise<{
    value?: string;
    from?: string;
    to?: string;
    result?: string;
    error?: string;
  }>;
};

export default async function LengthPage({ searchParams }: LengthPageProps) {
  const params = await searchParams;

  if (params.result) {
    const summary = `${params.value} ${params.from} = ${formatNumber(Number(params.result))} ${params.to}`;
    return <ResultCard summary={summary} resetHref="/length" />;
  }

  return (
    <>
      {params.error ? <p className="error">{params.error}</p> : null}
      <ConversionForm
        action={convertLengthAction}
        fieldLabel="Enter the length to convert"
        units={UNIT_OPTIONS}
      />
    </>
  );
}
