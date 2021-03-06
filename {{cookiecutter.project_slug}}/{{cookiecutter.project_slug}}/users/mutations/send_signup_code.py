from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class SendSignupCode(BaseMutation):
    """
    Sends a signup code to the given email.
    """

    class Input:
        email = String(required=True)

    @classmethod
    def perform_mutate(cls, root, info, email):
        # TODO: check if email already exists
        # TODO: send signup code to email
        return cls(success=True)
