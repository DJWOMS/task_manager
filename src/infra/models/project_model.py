from sqlalchemy.orm import Mapped
from src.infra.models.base_model import Base

from src.domain.project.constants import StatusProject


class ProjectModel(Base):
    __tablename__ = "projects"

    name: Mapped[str]
    description: Mapped[str]
    owner_id: Mapped[int]
    status: Mapped[StatusProject]
    # members
