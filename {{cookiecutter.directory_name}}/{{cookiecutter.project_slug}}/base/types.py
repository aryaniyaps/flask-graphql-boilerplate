from graphene import Interface, DateTime, ID


class BaseType(Interface):
    id = ID(required=True)
    created_at = DateTime(required=True)
    updated_at = DateTime(required=True)
