from flask_login import current_user
from graphene import ObjectType, Field, String

from .types import UserType


__all__ = (
    "UserQuery",
)


def resolve_viewer(root, info):
    if current_user.is_anonymous:
        return None
    return current_user


def resolve_user(root, info, username):
    loaders = info.context.get("loaders")
    return loaders.get("users_by_username").load(key=username)


class UserQuery(ObjectType):
    viewer = Field(
        type=UserType,
        resolver=resolve_viewer,
        description="The currently authenticated user."
    )
    user = Field(
        type=UserType,
        resolver=resolve_user,
        description="Look up an user by username.",
        username=String(
            required=True,
            description="The username of the user."
        )
    )
