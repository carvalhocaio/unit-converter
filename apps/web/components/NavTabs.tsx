"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

// This is the only client-rendered piece in the app. Its sole job is
// highlighting the active tab; form submissions still happen through
// classic server-rendered POST + redirect, with no client JS involved.
const TABS = [
  { href: "/length", label: "Length" },
  { href: "/weight", label: "Weight" },
  { href: "/temperature", label: "Temperature" },
] as const;

export function NavTabs() {
  const pathname = usePathname();

  return (
    <nav className="tabs">
      {TABS.map((tab) => (
        <Link key={tab.href} href={tab.href} data-active={pathname.startsWith(tab.href)}>
          {tab.label}
        </Link>
      ))}
    </nav>
  );
}
