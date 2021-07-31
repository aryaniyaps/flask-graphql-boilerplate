import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def current_user(self, input: LoginInput) -> bool:
        return True
