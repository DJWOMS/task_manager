from src.domain.project.interface import IProjectRepository
from src.domain.project.dtos.project_dto import CreateProjectDTO, UpdateProjectDTO, ProjectDTO


class ProjectUseCase:
    def __init__(self, repository: IProjectRepository) -> None:
        self.repository = repository

    async def create(self, dto: CreateProjectDTO) -> dict:
        await self.repository.create(dto)
        return {"status": "ok"}

    async def get_all(self) -> list[ProjectDTO]:
        return await self.repository.get_all()

    async def get(self, pk: int) -> ProjectDTO:
        return await self.repository.get(pk)

    async def update(self, pk: int, dto: UpdateProjectDTO) -> ProjectDTO:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(pk)
