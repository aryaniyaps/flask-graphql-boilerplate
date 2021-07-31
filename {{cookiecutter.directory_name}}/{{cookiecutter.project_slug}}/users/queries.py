import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def current_user(self) -> bool:
        return True
