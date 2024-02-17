from __future__ import annotations

from typing import TYPE_CHECKING, Any

__all__ = ["UseCase", "ServiceError"]


if TYPE_CHECKING:
    from litestar.contrib.repository import AbstractAsyncRepository, FilterTypes


class ServiceError(Exception):
    """Base class for `Service` related exceptions."""


class UseCase[ModelT]:
    def __init__(self, repository: AbstractAsyncRepository[ModelT]) -> None:
        self.repository = repository

    async def create(self, data: ModelT) -> ModelT:
        return await self.repository.add(data)

    async def update(self, id_: Any, data: ModelT) -> ModelT:
        return await self.repository.update(data)

    async def delete(self, id_: Any) -> ModelT:
        return await self.repository.delete(id_)

    async def list(self, *filters: FilterTypes, **kwargs: Any) -> list[ModelT]:
        return await self.repository.list(*filters, **kwargs)

    async def get(self, id_: Any) -> ModelT:
        return await self.repository.get(id_)


