from graphene import ObjectType, Field
from graphene.relay import Node

from .types import UserType


class UserQuery(ObjectType):
    viewer = Field(type=UserType)
    user = Node.Field(type=UserType)

    def resolve_viewer(root, info):
        """
        looks up the authenticated user.
        """
        pass
