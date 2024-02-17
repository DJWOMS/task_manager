from typing import Any
from uuid import UUID

import uvicorn
from litestar import Litestar
from litestar.exceptions import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api import create_router
from src.app.config import (
    cors,
    db,
    email,
    logging,
    openapi,
    project,
    security,
    sqlalchemy_plugin,
)

__all__ = ["create_app"]

from src.exception_handlers import not_found_exception_handler
from src.exceptions import NotFoundError


def create_app(**kwargs: Any) -> Litestar:
    kwargs.setdefault("debug", project.server.debug)

    return Litestar(
        route_handlers=[create_router()],
        plugins=[sqlalchemy_plugin.plugin],
        signature_namespace={
            "AsyncSession": AsyncSession,
        },
        exception_handlers={
            NotFoundError: not_found_exception_handler
        },
        **kwargs,
    )


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=project.server.host,
        log_level=project.server.log_level,
        port=project.server.port,
        reload=project.server.reload,
        timeout_keep_alive=project.server.keepalive,
        use_colors=project.server.use_colors,
    )
