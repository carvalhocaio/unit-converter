from urllib.parse import urlencode

from fastapi import APIRouter, Form, Query, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .categories import ConversionCategory
from .format import format_number
from .validation import parse_finite_float

_INVALID_INPUT_ERROR = "Please enter a valid number and choose valid units"


def build_conversion_router(
    category: ConversionCategory, templates: Jinja2Templates
) -> APIRouter:
    router = APIRouter()
    path = f"/{category.slug}"

    @router.get(path, response_class=HTMLResponse, name=f"{category.slug}_get")
    async def get_page(
        request: Request,
        value: str | None = None,
        from_: str | None = Query(default=None, alias="from"),
        to: str | None = None,
        result: str | None = None,
        error: str | None = None,
    ) -> HTMLResponse:
        context = {
            "request": request,
            "category": category,
            "categories": request.app.state.categories,
            "active_slug": category.slug,
            "error": error,
        }
        if result is not None:
            context["summary"] = (
                f"{value} {from_} = {format_number(float(result))} {to}"
            )
        return templates.TemplateResponse(request, "category.html", context)

    @router.post(path, name=f"{category.slug}_post")
    async def post_form(
        value: str = Form(...),
        from_: str = Form(..., alias="from"),
        to: str = Form(...),
    ) -> RedirectResponse:
        parsed_value = parse_finite_float(value)
        if (
            parsed_value is None
            or not category.is_unit(from_)
            or not category.is_unit(to)
        ):
            query = urlencode({"error": _INVALID_INPUT_ERROR})
            return RedirectResponse(
                f"{path}?{query}", status_code=status.HTTP_303_SEE_OTHER
            )

        result = category.convert(parsed_value, from_, to)
        query = urlencode(
            {"value": str(parsed_value), "from": from_, "to": to, "result": result}
        )
        return RedirectResponse(
            f"{path}?{query}", status_code=status.HTTP_303_SEE_OTHER
        )

    return router
