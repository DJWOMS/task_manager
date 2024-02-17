from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)

from src.app.config.db import settings


class DatabaseHelper:
    """Класс для работы с базой данных
    """

    def __init__(
            self,
            url: str,
            echo: bool,
            echo_pool: bool,
            max_overflow: int,
            pool_size: int,
            pool_timeout: int,
            pool_disable: NullPool
    ):
        self.engine = create_async_engine(
            url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
            pool_timeout=pool_timeout,
            poolclass=NullPool if pool_disable else None,
        )

        self.async_session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=AsyncSession
        )

    def get_scope_session(self):
        return async_scoped_session(
            session_factory=self.async_session_factory,
            scopefunc=current_task
        )

    @asynccontextmanager
    async def get_db_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.async_session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def get_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.async_session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DatabaseHelper(
    settings.database_url,
    settings.db_echo_log,
    settings.db_echo_pool,
    settings.db_pool_max_overflow,
    settings.db_pool_size,
    settings.db_pool_timeout,
    settings.db_pool_disable
)
