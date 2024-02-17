from litestar import Router

from .healthcheck_controller import healthcheck


__all__ = ["health_check"]


health_check = Router(path="/system", route_handlers=[healthcheck], tags=["system"])
