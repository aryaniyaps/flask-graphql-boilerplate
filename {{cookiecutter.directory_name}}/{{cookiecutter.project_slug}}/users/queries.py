import strawberry


class UserQuery:
    @strawberry.field
    def current_user(self) -> bool:
        return True
    
    @strawberry.field
    def user(self, id: strawberry.ID) -> bool:
        return True
