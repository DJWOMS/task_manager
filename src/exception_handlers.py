from litestar import Request, Response, MediaType

from src.exceptions import NotFoundError


def not_found_exception_handler(request: Request, exc: NotFoundError) -> Response:
    return Response(
        media_type=MediaType.TEXT,
        content=f"{exc.detail}",
        status_code=404,
    )
