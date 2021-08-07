from graphene import String

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation


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
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)
