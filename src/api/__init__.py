from litestar import Router

from .system import health_check
from .v1 import (
    user_controller,
    project_controller,
)

__all__ = ["create_router"]


def create_router() -> Router:
    return Router(
        path="/v1",
        route_handlers=[
            health_check,
            # user_controller.UserController,
            project_controller.ProjectController,
        ]
    )
