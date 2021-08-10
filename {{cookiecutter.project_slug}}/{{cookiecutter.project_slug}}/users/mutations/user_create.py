from flask_login import login_user
from graphene import String, Boolean, Field

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
        remember = Boolean(
            default_value=True,
            description="Remembers the user after session expires."
        )

    user = Field(
        type=UserType,
        description="The created user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):        
        user = User(
            email=data.get("email"), 
            username=data.get("username")
        )
        user.set_password(data.get("password"))
        user.save()

        login_user(
            user=user, 
            remember=data.get("remember")
        )

        return cls(
            success=True,
            user=user
        )
