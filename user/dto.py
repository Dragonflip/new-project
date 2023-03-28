import dataclasses
from typing import Any
from django.contrib.auth.models import User


@dataclasses.dataclass
class UserDataClass:
    username: str
    first_name: str
    last_name: str
    email: str
    id: int | Any = None
    password: str | Any = None

    @classmethod
    def from_instance(cls, user: User):
        return cls(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
        )
