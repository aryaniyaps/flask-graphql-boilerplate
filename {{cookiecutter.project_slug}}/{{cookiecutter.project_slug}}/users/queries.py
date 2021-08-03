from graphene import ObjectType, Field
from graphene.relay import Node

from .types import UserType


def resolve_viewer(root, info):
    pass


class UserQuery(ObjectType):
    user = Node.Field(
        type=UserType,
        description="Look up an user by ID."
    )
    viewer = Field(
        type=UserType,
        resolver=resolve_viewer,
        description="Look up the current user."
    )
