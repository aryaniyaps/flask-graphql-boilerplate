from flask import render_template
from flask_login import current_user, login_user
from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.emails import send_mail
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
        password = data.get("password")
        user = User()
        # TODO: check email and reset token.
        # TODO: validate new password.
        user.set_password(password)
        user.save()
        login_user(user=user)
        send_mail(
            to=current_user.email,
            subject="Password Changed",
            template=render_template(
                "emails/password_changed.html",
                user=current_user
            )
        )
        return cls(success=True)
