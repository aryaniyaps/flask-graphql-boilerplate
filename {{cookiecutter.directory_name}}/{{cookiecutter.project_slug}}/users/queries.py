from graphene import ObjectType, Field, ID

from .types import UserType


class UserQuery(ObjectType):
    user = Field(UserType, id=ID(required=True))
    viewer = Field(UserType)

    def resolve_user(root, info, id):
        """
        looks up an user with the given ID.
        """
        return UserType.get_node(info=info, id=id)

    def resolve_viewer(root, info):
        """
        looks up the authenticated user.
        """
        pass
