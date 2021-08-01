import strawberry
from strawberry.file_uploads import Upload

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


@strawberry.input
class ResetPasswordInput:
    password: str
    reset_token: str


@strawberry.input
class RequestResetInput:
    email: str


@strawberry.input
class UpdateUserInput:
    avatar: Upload
    username: str


@strawberry.input
class ChangeEmailInput:
    email: str
    change_code: str


@strawberry.input
class RequestEmailChangeInput:
    email: str


@strawberry.type
class LoginPayload:
    pass


@strawberry.type
class RegisterPayload:
    pass