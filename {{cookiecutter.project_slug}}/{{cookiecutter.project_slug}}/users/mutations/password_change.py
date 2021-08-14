from flask import render_template
from flask_login import current_user, logout_user
from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.extensions import db
from {{ cookiecutter.project_slug }}.emails import send_mail


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
    def perform_mutate(cls, root, info, **data):
        new_password = data.get("new_password")
        old_password = data.get("old_password")
        if not current_user.check_password(old_password):
            # TODO: handle errors here.
            pass
        # TODO: validate new password here.
        current_user.set_password(new_password)
        db.session.commit()
        # logout existing user sessions.
        logout_user()
        send_mail(
            to=current_user.email,
            subject="Password Changed",
            template=render_template(
                "emails/password_changed.html",
                user=current_user
            )
        )
        return cls(success=True)
