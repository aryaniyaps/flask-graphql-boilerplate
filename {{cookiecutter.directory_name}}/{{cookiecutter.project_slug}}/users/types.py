import strawberry

from {{ cookiecutter.project_slug }}.base.types import BaseType


@strawberry.type
class UserType(BaseType):
    email: str
    username: str
    password: str
    avatar: str


@strawberry.input
class LoginInput:
    email: str
    password: str


@strawberry.input
class RegisterInput:
    email: str
    username: str
    password: str


@strawberry.type
class LoginPayload:
    pass


@strawberry.type
class RegisterPayload:
    pass