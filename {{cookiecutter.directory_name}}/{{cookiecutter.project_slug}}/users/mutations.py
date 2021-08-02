from graphene import String, ObjectType
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class Register(BaseMutation):
    """
    creates an user instance.
    """
    class Input:
        email = String(required=True)
        username = String(required=True)
        password = String(required=True)


class Login(BaseMutation):
    """
    logs the user associated with the provided
    credentials in, if they were correct.
    """
    class Input:
        email = String(required=True)
        password = String(required=True)


class ResetPassword(BaseMutation):
    """
    resets the password for the user account
    associated with the given email address.
    """
    class Input:
        password = String(required=True)
        reset_token = String(required=True)
        email = String(required=True)


class RequestPasswordReset(BaseMutation):
    """
    sends a password reset link to the
    provided email address.
    """
    class Input:
        email = String(required=True)


class UpdateCurrentUser(BaseMutation):
    """
    updates the current user instance.
    """
    class Input:
        avatar = Upload()
        username = String()


class RequestEmailChange(BaseMutation):
    """
    sends a email change link to the
    provided email address.
    """
    class Input:
        email = String(required=True)


class ChangeEmail(BaseMutation):
    """
    changes the email for the user account
    associated with the given email address.
    """
    class Input:
        email = String(required=True)
        change_code = String(required=True)


class UserMutation(ObjectType):
    register = Register.Field()
    login = Login.Field()
    reset_password = ResetPassword.Field()
    request_password_reset = RequestPasswordReset.Field()
    update_current_user = UpdateCurrentUser.Field()
    request_email_change = RequestEmailChange.Field()
    change_email = ChangeEmail.Field()
