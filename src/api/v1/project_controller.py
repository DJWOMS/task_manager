from litestar import Controller, post, get, put, delete, status_codes
from litestar.di import Provide
from litestar.dto import DTOData
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.project.project_usecase import ProjectUseCase
from src.domain.project.dtos.project_dto import CreateProjectDTO, UpdateProjectDTO, ProjectDTO
from src.infra.repositories.project_repository import ProjectRepositoryImpl


def provides_usecase(db_session: AsyncSession) -> ProjectUseCase:
    return ProjectUseCase(ProjectRepositoryImpl(session=db_session))


class ProjectController(Controller):
    path = "/project"
    dependencies = {"service": Provide(provides_usecase, sync_to_thread=False)}
    tags = ["project"]

    @post("/")
    async def create(self, data: CreateProjectDTO, service: ProjectUseCase) -> dict:
        return await service.create(data)

    @get("/")
    async def get_all(self, service: ProjectUseCase) -> list[ProjectDTO]:
        return await service.get_all()

    @get("/{pk:int}")
    async def get(self, pk: int, service: ProjectUseCase) -> ProjectDTO:
        return await service.get(pk)

    @put("/{pk:int}")
    async def update(self, pk: int, data: UpdateProjectDTO, service: ProjectUseCase) -> ProjectDTO:
        return await service.update(pk, data)

    @delete("/{pk:int}", status_code=status_codes.HTTP_204_NO_CONTENT)
    async def delete(self, pk: int, service: ProjectUseCase) -> None:
        return await service.delete(pk)
