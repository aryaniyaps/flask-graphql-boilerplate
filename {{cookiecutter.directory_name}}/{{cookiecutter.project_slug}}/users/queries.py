import strawberry


class UserQuery:
    @strawberry.field
    def current_user(self) -> bool:
        """
        looks up the authenticated user.
        """
        return True
    
    @strawberry.field
    def user(self, id: strawberry.ID) -> bool:
        """
        looks up an user with the given ID.
        """
        return True
