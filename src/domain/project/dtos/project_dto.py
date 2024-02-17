from pydantic import BaseModel, Field

from src.domain.project.constants import StatusProject


class ProjectBaseDTO(BaseModel):
    name: str = Field(max_length=20, min_length=3)
    description: str = Field(max_length=500)
    owner_id: int
    status: StatusProject


class CreateProjectDTO(ProjectBaseDTO):
    name: str = Field(max_length=20, min_length=3)
    description: str
    owner_id: int
    # members: list[int] | None = None
    status: StatusProject = StatusProject.ACTIVE


class UpdateProjectDTO(CreateProjectDTO):
    pass


class ProjectDTO(ProjectBaseDTO):
    id: int
    members: list[int] | None = None
    logo: str | None = None
