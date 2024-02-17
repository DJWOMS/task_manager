from litestar import Router, get


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"health": "OK"}


system_routes = Router(path="/system", route_handlers=[healthcheck])
