from graphene import String, Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.types import UserType


class Authenticate(BaseMutation):
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
                user_errors=(
                    dict(
                        field="email",
                        message="Incorrect email provided."
                    ),
                )
            )

        if not user.check_password(password):
            return cls(
                success=False,
                user_errors=(
                    dict(
                        field="password",
                        message="Incorrect password provided."
                    ),
                )
            )

        if user.has_stale_password():
            # recalculate the user's password hash.
            user.set_password(password)
            user.save()
        
        # TODO: return access and refresh tokens
        # after logging an user in.
        return cls(
            success=True,
            user=user,
            access_token="",
            refresh_token=""
        )
