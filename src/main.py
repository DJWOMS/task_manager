from typing import Any
from uuid import UUID

import uvicorn
from litestar import Litestar
from litestar.contrib.repository import FilterTypes
from litestar.contrib.repository.exceptions import RepositoryError as RepositoryException
from litestar.contrib.repository.filters import (
    BeforeAfter,
    CollectionFilter,
    LimitOffset,
    OrderBy,
    SearchFilter,
)
from litestar.stores.registry import StoreRegistry
from sqlalchemy.ext.asyncio import AsyncSession

# from app.controllers import create_router
from src.app.config import (
    cors,
    db,
    email,
    logging,
    openapi,
    project,
    security,
)

__all__ = ["create_app"]


# dependencies = create_collection_dependencies()


def create_app(**kwargs: Any) -> Litestar:
    kwargs.setdefault("debug", project.server.debug)

    return Litestar(
        # response_cache_config=cache.config,
        # dependencies=dependencies,
        # exception_handlers={
        #     RepositoryException: exceptions.repository_exception_to_http_response,  # type: ignore[dict-item]
        #     ServiceError: exceptions.service_exception_to_http_response,  # type: ignore[dict-item]
        # },
        # logging_config=logging.settings.log_config,
        # openapi_config=openapi.settings.config,
        # route_handlers=[health_check, create_router()],
        # on_shutdown=[redis.close],
        # on_startup=[sentry.configure],
        # plugins=[sqlalchemy_plugin.plugin],
        signature_namespace={
            "AsyncSession": AsyncSession,
            # "FilterTypes": FilterTypes,
            # "BeforeAfter": BeforeAfter,
            # "CollectionFilter": CollectionFilter,
            # "LimitOffset": LimitOffset,
            # "UUID": UUID,
            # "OrderBy": OrderBy,
            # "SearchFilter": SearchFilter,
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
