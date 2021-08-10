from graphene import relay
from graphene_mongo import MongoengineObjectType

from .loaders import UserLoader
from .models import User


class UserType(MongoengineObjectType):
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
        """
        Loads an user within a batch.
        """
        return UserLoader().load(key=id)
