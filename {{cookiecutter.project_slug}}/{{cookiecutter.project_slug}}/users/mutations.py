from graphene import String, Field, ObjectType
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from .types import UserType


class Login(BaseMutation):
    """
    Logs the user associated with the provided
    credentials in, if they were correct.
    """
    class Input:
        email = String(
            required=True,
            description="The email of the user."
        )
        password = String(
            required=True,
            description="The password of the user."
        )
    
    access_token = String(
        required=True
    )
    refresh_token = String(
        required=True
    )


class CreateUser(BaseMutation):
    """
    Creates an user instance.
    """
    class Input:
        email = String(
            required=True,
            description="The email of the user."
        )
        username = String(
            required=True,
            description="The username of the user."
        )
        password = String(
            required=True,
            description="The password of the user."
        )

    user = Field(
        required=True, 
        type=UserType
    )
    # TODO: return access and refresh tokens
    # after creating an user.


class ResetPassword(BaseMutation):
    """
    Resets the password for the user account
    associated with the given email address.
    """
    class Input:
        password = String(
            required=True,
            description="The new password for the user account."
        )
        reset_token = String(
            required=True,
            description="The password reset token."
        )
        email = String(
            required=True,
            description="The email of the user account."
        )
    
    # TODO: login user after resetting password.


class RequestPasswordReset(BaseMutation):
    """
    Sends a password reset link to the
    provided email address.
    """
    class Input:
        email = String(
            required=True,
            description="The email to send the password reset link to."
        )


class UpdateCurrentUser(BaseMutation):
    """
    Updates the current user instance.
    """
    class Input:
        avatar = Upload(
            description="The user's new avatar file."
        )
        username = String(
            description="The user's new username."
        )
    
    user = Field(
        required=True, 
        type=UserType
    )


class RequestEmailChange(BaseMutation):
    """
    Sends a email change link to the
    provided email address.
    """
    class Input:
        email = String(
            required=True,
            description="The email to send the email change link to."
        )


class ChangeEmail(BaseMutation):
    """
    Changes the email for the user account
    associated with the given email address.
    """
    class Input:
        email = String(
            required=True,
            description="The old email of the user account."
        )
        change_code = String(
            required=True,
            description="The email change code."
        )

    user = Field(
        required=True, 
        type=UserType
    )


class ChangePassword(BaseMutation):
    """
    Changes the current user's password, if
    the provided password was correct.
    """
    class Input:
        new_password = String(
            required=True,
            description="The new password for the account."
        )
        old_password = String(
            required=True,
            description="The old password for the account."
        )


class UserMutation(ObjectType):
    login = Login.Field()
    create_user = CreateUser.Field()
    reset_password = ResetPassword.Field()
    request_password_reset = RequestPasswordReset.Field()
    update_current_user = UpdateCurrentUser.Field()
    request_email_change = RequestEmailChange.Field()
    change_email = ChangeEmail.Field()
    change_password = ChangePassword.Field()
