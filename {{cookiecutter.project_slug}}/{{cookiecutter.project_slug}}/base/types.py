from graphene import ObjectType, String, List, NonNull


class ErrorType(ObjectType):
    """
    A set of error messages which map
    to a specific input field.
    """
    field = String(
        required=True,
        description="The field of the error."
    )
    messages = List(
        required=True,
        of_type=String,
        description="The messages of the error."
    )

    class Meta:
        name = "Error"
