"use server";

import { redirect } from "next/navigation";
import { convertLength, isLengthUnit } from "@repo/units";

// Handles the length conversion form submission. Validates the raw
// FormData, computes the result via the pure @repo/units domain, and
// redirects back to the same route with the outcome encoded in the
// query string (Post/Redirect/Get — no client JS involved).
export async function convertLengthAction(formData: FormData): Promise<void> {
  const value = Number(formData.get("value"));
  const from = String(formData.get("from"));
  const to = String(formData.get("to"));

  if (!Number.isFinite(value) || !isLengthUnit(from) || !isLengthUnit(to)) {
    redirect("/length?error=Please+enter+a+valid+number+and+choose+valid+units");
  }

  const result = convertLength(value, from, to);

  const params = new URLSearchParams({
    value: String(value),
    from,
    to,
    result: String(result),
  });

  redirect(`/length?${params.toString()}`);
}
