from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    first_name: str
    last_name: str
    id: UUID
