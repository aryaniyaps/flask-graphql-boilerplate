from graphene import String, Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class Unauthenticate(BaseMutation):
    """
    Logs the current user out.
    """
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)
