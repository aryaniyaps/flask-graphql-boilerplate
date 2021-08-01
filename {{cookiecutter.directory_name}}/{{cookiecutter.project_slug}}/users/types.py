from graphene import InputObjectType, ObjectType, String
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.types import BaseType


class UserType(ObjectType):
    email = String(required=True)
    username = String(required=True)
    password = String(required=True)

    class Meta:
        name = "User"
        interfaces = (BaseType,)


class LoginInput(InputObjectType):
    email = String(required=True)
    password = String(required=True)


class RegisterInput(InputObjectType):
    email = String(required=True)
    username = String(required=True)
    password = String(required=True)


class ResetPasswordInput(InputObjectType):
    password = String(required=True)
    reset_token = String(required=True)


class RequestResetInput(InputObjectType):
    email = String(required=True)


class UpdateUserInput(InputObjectType):
    avatar = Upload()
    username = String()


class RequestEmailChangeInput(InputObjectType):
    email = String(required=True)


class ChangeEmailInput(InputObjectType):
    email = String(required=True)
    change_code = String(required=True)
