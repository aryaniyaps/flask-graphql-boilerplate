from graphene import ObjectType, String


class ErrorType(ObjectType):
    """
    an error message which maps to a
    specific input field.
    """
    field = String(required=True)
    message = String(required=True)

    class Meta:
        name = "Error"
