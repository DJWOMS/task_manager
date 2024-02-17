from sqlalchemy.orm import Mapped
from src.infra.models.base_model import Base


class ProjectModel(Base):
    __tablename__ = "projects"

    name: Mapped[str]
    description: Mapped[str]
