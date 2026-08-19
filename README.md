# Unit Converter

A simple web app to convert values between different units of length, weight, and temperature.

Built as part of the [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter).

## Stack

- **[Next.js 15](https://nextjs.org/)** (App Router) + React 19 — server-rendered pages, Server Actions for form handling
- **TypeScript** end to end
- **[Turborepo](https://turbo.build/)** + **pnpm workspaces** — monorepo orchestration
- **[Vitest](https://vitest.dev/)** — unit tests for the conversion domain

## Project structure

```
unit-converter/
├── apps/
│   └── web/               # Next.js app — routes, forms, presentation
│       └── app/
│           ├── length/
│           ├── weight/
│           └── temperature/
└── packages/
    └── units/             # Pure conversion domain, framework-agnostic
        └── src/
            ├── length.ts
            ├── weight.ts
            └── temperature.ts
```

## Architecture

The project is split into two layers:

- **`packages/units`** is the domain layer: pure TypeScript functions (`convertLength`, `convertWeight`, `convertTemperature`) with no knowledge of HTTP, forms, or React. Each unit category exports a `Record`-based conversion table (or, for temperature, a Celsius-based intermediate step, since it involves offsets rather than a pure multiplicative factor) and a type guard (`isLengthUnit`, etc.) used to validate untyped input at the HTTP boundary. This layer is fully covered by unit tests and has zero external dependencies.

- **`apps/web`** is the presentation layer. Each unit category (`length`, `weight`, `temperature`) follows the same **Post/Redirect/Get** pattern:
  1. `page.tsx` (Server Component) reads `searchParams` — if a `result` is present, it renders `ResultCard`; otherwise, it renders `ConversionForm`.
  2. `actions.ts` (`"use server"`) receives the submitted `FormData`, validates it against the domain's type guards, computes the result via `@repo/units`, and `redirect()`s back to the same route with the outcome encoded in the query string.

This means form submissions are handled with **no client-side JavaScript, no `fetch`, no `useState`** — just a native HTML form POST intercepted by a Server Action, matching the classic `target="_self"` submission flow described in the original project spec. The only client-rendered piece in the whole app is `NavTabs`, whose sole job is highlighting the active tab via `usePathname`.

## Getting started

```bash
pnpm install
pnpm dev
```

The app runs at `http://localhost:3000` (or the next available port).

## Testing

```bash
pnpm test
```

Runs the `packages/units` test suite via Vitest, covering length, weight, and temperature conversions.

## Build

```bash
pnpm build
```
