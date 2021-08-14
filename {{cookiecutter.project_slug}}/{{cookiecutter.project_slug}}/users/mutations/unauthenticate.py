from flask_login import logout_user

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class Unauthenticate(BaseMutation):
    """
    Logs the current user out.
    """
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        logout_user()
        return cls(success=True)
