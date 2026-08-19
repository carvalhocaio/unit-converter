import { WEIGHT_UNITS } from "@repo/units";
import { ConversionForm } from "@/components/ConversionForm";
import { ResultCard } from "@/components/ResultCard";
import { capitalize, formatNumber } from "@/lib/format";
import { convertWeightAction } from "./actions";

const UNIT_OPTIONS = WEIGHT_UNITS.map((unit) => ({ value: unit, label: capitalize(unit) }));

type WeightPageProps = {
  searchParams: Promise<{
    value?: string;
    from?: string;
    to?: string;
    result?: string;
    error?: string;
  }>;
};

export default async function WeightPage({ searchParams }: WeightPageProps) {
  const params = await searchParams;

  if (params.result) {
    const summary = `${params.value} ${params.from} = ${formatNumber(Number(params.result))} ${params.to}`;
    return <ResultCard summary={summary} resetHref="/weight" />;
  }

  return (
    <>
      {params.error ? <p className="error">{params.error}</p> : null}
      <ConversionForm
        action={convertWeightAction}
        fieldLabel="Enter the weight to convert"
        units={UNIT_OPTIONS}
      />
    </>
  );
}
