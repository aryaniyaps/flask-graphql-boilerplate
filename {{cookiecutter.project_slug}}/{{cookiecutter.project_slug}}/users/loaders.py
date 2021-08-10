from aiodataloader import DataLoader

from .models import User

__all__ = (
    "user_loader",
    "user_by_username_loader"
)


async def get_users(keys):
    return [User.objects(id=user_id).first() for user_id in keys]

async def get_users_by_username(keys):
    return [User.objects(username=username).first() for username in keys]


user_loader = DataLoader(
    batch_load_fn=get_users
)

user_by_username_loader = DataLoader(
    batch_load_fn=get_users_by_username
)
