from flask import render_template
from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.emails import send_mail
from {{ cookiecutter.project_slug }}.users.models import User


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
