from flask_login import current_user
from graphene import String, Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.types import UserType


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
        email = data.get("email")
        password = data.get("password")
        if not current_user.check_password(password):
            # TODO: handle errors here.
            pass
        # TODO: validate change code and email here.
        current_user.email = email
        current_user.save()
        return cls(
            success=True,
            user=current_user
        )
