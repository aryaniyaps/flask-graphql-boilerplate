from flask_login import current_user
from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.extensions import db


class UserDeactivate(BaseMutation):
    """
    Deactivates the current user.
    """
    class Input:
        password = String(required=True)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        # TODO: check user's password.
        current_user.is_active = False
        db.session.commit()
        return cls(success=True)
