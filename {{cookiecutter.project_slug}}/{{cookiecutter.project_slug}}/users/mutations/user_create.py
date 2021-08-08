from graphene import String, Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.types import UserType


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
                user_errors=(
                    dict(
                        field="email",
                        message="Email already exists."
                    ),
                )
            )
        
        if User.objects(username=username):
            return cls(
                success=False,
                user_errors=(
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
        user.set_password(password)
        user.save()

        # TODO: return access and refresh tokens
        # after creating an user.
        return cls(
            success=True,
            user=user
        )
