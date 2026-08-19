"use server";

import { redirect } from "next/navigation";
import { convertTemperature, isTemperatureUnit } from "@repo/units";

// Same Post/Redirect/Get pattern as length and weight.
export async function convertTemperatureAction(formData: FormData): Promise<void> {
  const value = Number(formData.get("value"));
  const from = String(formData.get("from"));
  const to = String(formData.get("to"));

  if (!Number.isFinite(value) || !isTemperatureUnit(from) || !isTemperatureUnit(to)) {
    redirect("/temperature?error=Please+enter+a+valid+number+and+choose+valid+units");
  }

  const result = convertTemperature(value, from, to);

  const params = new URLSearchParams({
    value: String(value),
    from,
    to,
    result: String(result),
  });

  redirect(`/temperature?${params.toString()}`);
}
