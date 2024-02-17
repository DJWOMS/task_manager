from litestar import get


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"health": "OK"}
