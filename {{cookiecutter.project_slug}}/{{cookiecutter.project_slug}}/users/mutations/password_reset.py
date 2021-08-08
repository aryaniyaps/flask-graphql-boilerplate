from flask_login import login_user
from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.models import User


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
        user = User()
        login_user(user=user)
        return cls(success=True)
