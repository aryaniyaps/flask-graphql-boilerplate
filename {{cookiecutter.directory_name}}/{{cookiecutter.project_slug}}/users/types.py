from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import User


class UserType(SQLAlchemyObjectType):
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
