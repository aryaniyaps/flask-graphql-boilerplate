from flask_login import current_user

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class UserInactivate(BaseMutation):
    """
    Inactivates the current user.
    """
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        current_user.inactivate()
        return cls(success=True)
