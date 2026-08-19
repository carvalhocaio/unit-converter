import { redirect } from "next/navigation";

// The root route has no content of its own; it simply lands the user
// on the first conversion category.
export default function HomePage() {
  redirect("/length");
}
