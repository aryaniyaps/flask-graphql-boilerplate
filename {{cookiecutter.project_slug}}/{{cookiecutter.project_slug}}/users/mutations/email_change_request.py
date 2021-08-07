from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


class EmailChangeRequest(BaseMutation):
    """
    Sends a email change link to the
    provided email address.
    """

    class Input:
        email = String(
            required=True,
            description="The email to send the email change link to."
        )
        password = String(
            required=True,
            description="The user account's password."
        )
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)
