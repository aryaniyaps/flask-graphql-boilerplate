from flask_login import login_user
from graphene import String, Boolean, Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.extensions import db
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
        remember = Boolean(
            default_value=True,
            description="Remembers the user after session expires."
        )
    
    user = Field(
        type=UserType,
        description="The current user instance."
    )

    @classmethod
    def perform_mutate(cls, root, info, email, password, remember):
        user = User.query.get(email=email)
        if user is None:
            return cls(
                success=False,
                user_errors=(
                    list(
                        dict(
                            field="email",
                            message="Incorrect email provided."
                        )
                    ),
                )
            )

        if not user.check_password(password):
            return cls(
                success=False,
                user_errors=(
                    list(
                        dict(
                            field="password",
                            message="Incorrect password provided."
                        )
                    ),
                )
            )

        if user.has_stale_password():
            # recalculate the user's password hash.
            user.set_password(password)
            db.session.commit()
        
        login_user(
            user=user, 
            remember=remember
        )        

        return cls(
            success=True,
            user=user
        )
