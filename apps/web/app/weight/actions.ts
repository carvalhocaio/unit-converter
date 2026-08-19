"use server";

import { redirect } from "next/navigation";
import { convertWeight, isWeightUnit } from "@repo/units";

// Handles the weight conversion form submission. Same Post/Redirect/Get
// pattern as the length route: validate, compute via @repo/units, redirect
// with the outcome in the query string.
export async function convertWeightAction(formData: FormData): Promise<void> {
  const value = Number(formData.get("value"));
  const from = String(formData.get("from"));
  const to = String(formData.get("to"));

  if (!Number.isFinite(value) || !isWeightUnit(from) || !isWeightUnit(to)) {
    redirect("/weight?error=Please+enter+a+valid+number+and+choose+valid+units");
  }

  const result = convertWeight(value, from, to);

  const params = new URLSearchParams({
    value: String(value),
    from,
    to,
    result: String(result),
  });

  redirect(`/weight?${params.toString()}`);
}
