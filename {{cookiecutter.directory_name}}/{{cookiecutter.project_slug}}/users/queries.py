import strawberry

from {{ cookiecutter.project_slug }}.base.permissions import IsAuthenticated


class UserQuery:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def current_user(self) -> bool:
        """
        looks up the authenticated user.
        """
        return True
    
    @strawberry.field(permission_classes=[IsAuthenticated])
    def user(self, id: strawberry.ID) -> bool:
        """
        looks up an user with the given ID.
        """
        return True
