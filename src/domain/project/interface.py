from abc import abstractmethod
from typing import Protocol

from src.domain.project.request_dtos.project_dto import CreateProjectDTO, UpdateProjectDTO
from src.domain.project.response_dtos.project_dto import ProjectDTO


class IProjectRepository(Protocol):

    model = None

    @abstractmethod
    async def create(self, dto: CreateProjectDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[ProjectDTO]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, pk: int) -> ProjectDTO:
        raise NotImplementedError

    @abstractmethod
    async def update(self, pk: int, dto: UpdateProjectDTO) -> ProjectDTO:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, pk: int) -> None:
        raise NotImplementedError
