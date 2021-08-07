from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from flask import render_template
from graphene import String, Field, ObjectType
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.emails import send_mail
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
        description="The access token for the user."
    )
    refresh_token = String(
        description="The refresh token for the user."
    )
    user = Field(
        type=UserType,
        description="The current user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, password):
        user = User.objects(email=email).first()
        if not user:
            return cls(
                success=False,
                errors=(
                    dict(
                        field="email",
                        message="Incorrect email provided."
                    ),
                )
            )

        try:
            password_hasher.verify(user.password, password)
        except VerificationError:
            return cls(
                success=False,
                errors=(
                    dict(
                        field="password",
                        message="Incorrect password provided."
                    ),
                )
            )

        if password_hasher.check_needs_rehash(user.password):
            # recalculate the user's password hash.
            user.password = password_hasher.hash(password)
            user.save()
        
        # TODO: return access and refresh tokens
        # after logging an user in.
        return cls(
            success=True,
            user=user,
            access_token="",
            refresh_token=""
        )


class UserCreate(BaseMutation):
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
        code = String(
            required=True,
            description="The email confirmation code."
        )

    access_token = String(
        description="The access token for the user."
    )
    refresh_token = String(
        description="The refresh token for the user."
    )
    user = Field(
        type=UserType,
        description="The created user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, username, password):
        if User.objects(email=email):
            return cls(
                success=False,
                errors=(
                    dict(
                        field="email",
                        message="Email already exists."
                    ),
                )
            )
        
        if User.objects(username=username):
            return cls(
                success=False,
                errors=(
                    dict(
                        field="username",
                        message="Username already exists."
                    ),
                )
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

        # TODO: return access and refresh tokens
        # after creating an user.
        return cls(
            success=True,
            user=user
        )


class PasswordReset(BaseMutation):
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

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        # TODO: login user after resetting password.
        return cls(success=True)


class PasswordResetRequest(BaseMutation):
    """
    Sends a password reset link to the
    provided email, if it actually exists.
    """

    class Input:
        email = String(
            required=True,
            description="The email to send the password reset link to."
        )
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, email):
        user = User.objects(email=email).first()
        if user is not None:
            # TODO: generate a reset token.
            reset_token = "RESET_TOKEN"
            send_mail(
                to=user.email,
                subject="Reset Password",
                template=render_template(
                    "emails/password_reset.html",
                    token=reset_token
                )
            )
        return cls(success=True)


class CurrentUserUpdate(BaseMutation):
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
        type=UserType,
        description="The updated user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)


class EmailChangeRequest(BaseMutation):
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
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)


class EmailChange(BaseMutation):
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
        type=UserType,
        description="The updated user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)


class PasswordChange(BaseMutation):
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
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)


class UserMutation(ObjectType):
    login = Login.Field()
    user_create = UserCreate.Field()
    password_reset = PasswordReset.Field()
    password_reset_request = PasswordResetRequest.Field()
    current_user_update = CurrentUserUpdate.Field()
    email_change_request = EmailChangeRequest.Field()
    email_change = EmailChange.Field()
    password_change = PasswordChange.Field()
