import datetime
import jwt
from django.conf import settings
import dataclasses
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from typing import Any


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


def create_user(user: UserDataClass):
    instance = User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )
    instance.set_password(user.password)
    instance.save()
    return UserDataClass.from_instance(instance)


def get_user_from_username(username:str):
    return get_object_or_404(User, username=username) 

def create_token(user:User):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    return token
