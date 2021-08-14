from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .loaders import UserByIDLoader
from .models import User


class UserType(SQLAlchemyObjectType):
    """
    An individual user account.
    """
    class Meta:
        name = "User"
        model = User
        exclude_fields = (
            "password",
            "is_active"
        )
        interfaces = (
            relay.Node,
        )

    @classmethod
    def get_node(cls, info, id):
        loader = UserByIDLoader(info.context)
        return loader.load(key=id)
