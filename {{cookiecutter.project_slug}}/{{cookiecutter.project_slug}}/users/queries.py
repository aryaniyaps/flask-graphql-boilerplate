from flask_login import current_user
from graphene import ObjectType, Field

from .types import UserType


__all__ = (
    "UserQuery",
)


def resolve_viewer(root, info):
    return current_user


class UserQuery(ObjectType):
    viewer = Field(
        type=UserType,
        resolver=resolve_viewer,
        description="The currently authenticated user."
    )
