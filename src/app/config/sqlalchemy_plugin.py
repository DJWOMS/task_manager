from __future__ import annotations

from typing import TYPE_CHECKING, cast

from litestar.contrib.sqlalchemy.plugins.init import SQLAlchemyInitPlugin
from litestar.contrib.sqlalchemy.plugins.init.config import SQLAlchemyAsyncConfig
from litestar.contrib.sqlalchemy.plugins.init.config.common import (
    SESSION_SCOPE_KEY,
    SESSION_TERMINUS_ASGI_EVENTS,
)
from litestar.utils import delete_litestar_scope_state, get_litestar_scope_state

from src.app.config import project
from src.infra.database.db_helper import db_helper


if TYPE_CHECKING:
    from litestar.types.asgi_types import Message, Scope

__all__ = [
    "config",
    "plugin",
]


async def before_send_handler(message: Message, scope: Scope) -> None:
    session = cast("AsyncSession | None", get_litestar_scope_state(scope, SESSION_SCOPE_KEY))
    try:
        if session is not None and message["type"] == "http.response.start":
            if 200 <= message["status"] < 300:
                await session.commit()
            else:
                await session.rollback()
    finally:
        if session is not None and message["type"] in SESSION_TERMINUS_ASGI_EVENTS:
            await session.close()
            delete_litestar_scope_state(scope, SESSION_SCOPE_KEY)


config = SQLAlchemyAsyncConfig(
    session_dependency_key=project.server.api_db_session_dependency_key,
    engine_instance=db_helper.engine,
    session_maker=db_helper.async_session_factory,
    before_send_handler=before_send_handler,
)

plugin = SQLAlchemyInitPlugin(config=config)
