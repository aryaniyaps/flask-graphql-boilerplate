from graphene import InputObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_file_upload.scalars import Upload

from .models import User


class UserType(SQLAlchemyObjectType):
    class Meta:
        name = "User"
        model = User
        exclude_fields = (
            "password",
            "is_active"
        )


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
