from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class SendSignupCode(BaseMutation):
    """
    Sends a signup code to the given email.
    """
    class Input:
        email = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, email):
        return cls(success=True)
