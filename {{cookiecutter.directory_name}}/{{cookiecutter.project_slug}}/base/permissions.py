from strawberry.permission import BasePermission


class IsAuthenticated(BasePermission):
    message = "You're not authenticated."

    def has_permission(self, source, info) -> bool:
        return False
