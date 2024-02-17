from uuid import uuid4
from litestar import Controller, post, get, put, patch, delete, Router
from litestar.dto import DataclassDTO, DTOConfig, DTOData
from pydantic import UUID4

from src.domain.user.user_dto import User


class PartialUserDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"id"}, partial=True)


class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User:
        return data

    @get()
    async def list_users(self) -> list[User]:
        return [User(first_name="John", last_name="Doe", id=uuid4())]

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User:
        return User(first_name="John", last_name="Doe", id=user_id)

    @patch(path="/{user_id:uuid}", dto=PartialUserDTO)
    async def partial_update_user(
        self, user_id: UUID4, data: DTOData[User]
    ) -> User:
        return User(**data.__dict__, id=user_id)

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User: ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None: ...


user = Router(path="/", route_handlers=[UserController], tags=["user"])
