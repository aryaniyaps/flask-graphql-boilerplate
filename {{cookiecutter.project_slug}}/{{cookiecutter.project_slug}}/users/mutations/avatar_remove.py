from graphene import Field

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.types import UserType


class AvatarRemove(BaseMutation):
    """
    Removes the current user's avatar.
    """

    user = Field(
        type=UserType,
        description="The updated user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        return cls(success=True)
