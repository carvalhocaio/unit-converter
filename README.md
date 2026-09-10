# Unit Converter

A simple web app to convert values between different units of length, weight, and temperature.

Built as part of the [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter).

## Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — routes, forms, server-rendered HTML via Jinja2
- **Jinja2** — templates for the presentation layer
- **pytest** — unit and integration tests (TDD)
- **ruff** + **black** — linting and PEP-8 formatting

## Project structure

```
unit-converter/
├── src/unit_converter/
│   ├── units/             # Pure conversion domain, framework-agnostic
│   │   ├── linear.py       # Shared factor-based converter (length, weight)
│   │   ├── length.py
│   │   ├── weight.py
│   │   └── temperature.py  # Offset-based, kept separate from linear.py
│   └── web/                # FastAPI app — routes, templates, presentation
│       ├── app.py
│       ├── categories.py
│       ├── routes.py
│       ├── format.py
│       ├── validation.py
│       ├── templates/
│       └── static/
└── tests/
    ├── units/
    └── web/
```

## Architecture

The project is split into two layers:

- **`unit_converter.units`** is the domain layer: pure functions (`convert_length`,
  `convert_weight`, `convert_temperature`) with no knowledge of HTTP, forms, or
  templates. Length and weight share a generic `LinearUnitCategory` helper (a
  factor table relative to a base unit); temperature is kept separate since it
  involves offsets rather than a pure multiplicative factor. Each category also
  exposes a type guard (`is_length_unit`, etc.) used to validate untyped input
  at the HTTP boundary. This layer is fully covered by unit tests and has zero
  external dependencies.

- **`unit_converter.web`** is the presentation layer. All three categories
  (`length`, `weight`, `temperature`) are served by a **single generic route
  factory**, `build_conversion_router`, parameterized by a `ConversionCategory`
  config object (units, labels, validator, converter) — there is no per-category
  route code. Each category follows the same **Post/Redirect/Get** pattern:
  1. `GET /{category}` renders either the result (if `result` is present in the
     query string) or the form (plus an error message, if `error` is present).
  2. `POST /{category}` receives the submitted form data, validates it against
     the domain's type guards, computes the result, and redirects (303) back to
     the same route with the outcome encoded in the query string.

  This means form submissions are handled with **no client-side JavaScript** —
  just a native HTML form POST handled entirely on the server.

## Getting started

```bash
uv pip install -e ".[dev]"
uv run uvicorn unit_converter.web.app:app --reload
```

The app runs at `http://127.0.0.1:8000`.

## Testing

```bash
uv run pytest
```

Covers the `units` domain (length, weight, temperature conversions) and the
`web` layer (formatting/validation helpers, category config, and integration
tests against the FastAPI routes via `TestClient`).

## Linting & formatting

```bash
uv run ruff check .
uv run black --check .
```
