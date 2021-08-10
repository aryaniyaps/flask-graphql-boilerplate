from graphene import relay
from graphene_mongo import MongoengineObjectType

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
        loaders = info.context.get("loaders")
        return loaders.get("user_by_id").load(key=id)
