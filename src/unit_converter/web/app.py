from pathlib import Path

from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .categories import CATEGORIES
from .routes import build_conversion_router

_WEB_DIR = Path(__file__).parent
STATIC_DIR = _WEB_DIR / "static"
TEMPLATES_DIR = _WEB_DIR / "templates"


def create_app() -> FastAPI:
    app = FastAPI(title="Unit Converter")
    app.state.categories = CATEGORIES
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    templates = Jinja2Templates(directory=TEMPLATES_DIR)
    for category in CATEGORIES:
        app.include_router(build_conversion_router(category, templates))

    @app.get("/")
    async def root() -> RedirectResponse:
        return RedirectResponse(
            url="/length", status_code=status.HTTP_307_TEMPORARY_REDIRECT
        )

    return app


app = create_app()
