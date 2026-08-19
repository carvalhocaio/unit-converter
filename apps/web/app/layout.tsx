import type { ReactNode } from "react";
import { NavTabs } from "@/components/NavTabs";
import "./globals.css";

export const metadata = {
  title: "Unit Converter",
  description: "Convert between different units of length, weight, and temperature.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <main className="card">
          <h1>Unit Converter</h1>
          <NavTabs />
          {children}
        </main>
      </body>
    </html>
  );
}
