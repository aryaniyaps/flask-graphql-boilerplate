import strawberry

from .types import RegisterInput, LoginInput


class UserMutation:
    @strawberry.mutation
    def login(self, input: LoginInput) -> bool:
        return True
    
    @strawberry.mutation
    def register(self, input: RegisterInput) -> bool:
        return True

    @strawberry.mutation
    def reset_password(self) -> bool:
        return True
    
    @strawberry.mutation
    def send_password_reset(self) -> bool:
        return True
