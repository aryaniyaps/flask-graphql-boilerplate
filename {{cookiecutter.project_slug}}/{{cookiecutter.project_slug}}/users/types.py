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
