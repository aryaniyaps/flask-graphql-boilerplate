from graphene import ObjectType, String, List, NonNull


class ErrorType(ObjectType):
    """
    A set of error messages which map
    to a specific input field.
    """
    field = String(required=True)
    messages = List(
        required=True,
        of_type=NonNull(
            of_type=String
        )
    )

    class Meta:
        name = "Error"
