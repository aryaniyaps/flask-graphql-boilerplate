from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from graphene import String, Field, ObjectType
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from .models import User
from .types import UserType


password_hasher = PasswordHasher()


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
    user = Field(
        required=True, 
        type=UserType
    )

    @classmethod
    def perform_mutate(cls, root, info, email, password):
        user = User.objects(email=email).first()
        if not user:
            return cls(
                success=False,
                errors=[
                    dict(
                        field="email",
                        message="Incorrect email provided."
                    )
                ]
            )

        try:
            password_hasher.verify(user.password, password)
        except VerificationError:
            return cls(
                success=False,
                errors=[
                    dict(
                        field="password",
                        message="Incorrect password provided."
                    )
                ]
            )

        if password_hasher.check_needs_rehash(user.password):
            # recalculate the user's password hash.
            user.password = password_hasher.hash(password)
            user.save()
        
        # TODO: return access and refresh tokens
        # after loggin an user in.
        return cls(
            success=True,
            user=user,
            access_token="",
            refresh_token=""
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

    @classmethod
    def perform_mutate(cls, root, info, email, username, password):
        if User.objects(email=email):
            return cls(
                success=False,
                errors=[
                    dict(
                        field="email",
                        message="Email already exists."
                    )
                ]
            )
        
        if User.objects(username=username):
            return cls(
                success=False,
                errors=[
                    dict(
                        field="username",
                        message="Username already exists."
                    )
                ]
            )
        
        user = User(
            email=email, 
            username=username, 
            password=password
        )
        user.validate()
        # hash the user's password.
        user.password = password_hasher.hash(password)
        user.save()
        return cls(
            success=True,
            user=user
        )


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

    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


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
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


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

    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


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
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


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

    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


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
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        return cls(success=True)


class UserMutation(ObjectType):
    login = Login.Field()
    create_user = CreateUser.Field()
    reset_password = ResetPassword.Field()
    request_password_reset = RequestPasswordReset.Field()
    update_current_user = UpdateCurrentUser.Field()
    request_email_change = RequestEmailChange.Field()
    change_email = ChangeEmail.Field()
    change_password = ChangePassword.Field()
