from advanced_alchemy import wrap_sqlalchemy_exception
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.project.interface import IProjectRepository
from src.domain.project.dtos.project_dto import CreateProjectDTO, UpdateProjectDTO, ProjectDTO
from src.exceptions import NotFoundError
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from src.infra.models.project_model import ProjectModel


class ProjectRepositoryImpl(IProjectRepository):
    model = ProjectModel

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, dto: CreateProjectDTO) -> None:
        with wrap_sqlalchemy_exception():
            project = self.model(**dto.model_dump())
            self.session.add(project)
            await self.session.commit()

    async def get_all(self) -> list[ProjectDTO]:
        with wrap_sqlalchemy_exception():
            res = await self.session.execute(select(ProjectModel))
            projects = res.scalars().all()
            return [ProjectDTO(**project.__dict__) for project in projects]

    async def get(self, pk: int) -> ProjectDTO:
        with wrap_sqlalchemy_exception():
            result = await self.session.execute(select(ProjectModel).filter_by(id=pk))
            if project := result.scalar_one_or_none():
                return ProjectDTO(**project.__dict__)
            raise NotFoundError()

    async def update(self, pk: int, dto: UpdateProjectDTO) -> ProjectDTO:
        with wrap_sqlalchemy_exception():
            stmt = (
                update(self.model)
                .values(**dto.model_dump())
                .filter_by(id=pk)
                .returning(self.model)
            )
            res = await self.session.execute(stmt)
            await self.session.commit()
            project = res.scalar()
            return ProjectDTO(**project.__dict__)

    async def delete(self, pk: int) -> None:
        with wrap_sqlalchemy_exception():
            res = await self.session.execute(delete(self.model).filter_by(id=pk))
            if res.rowcount == 0:
                raise NotFoundError("Project not found")
            await self.session.commit()


