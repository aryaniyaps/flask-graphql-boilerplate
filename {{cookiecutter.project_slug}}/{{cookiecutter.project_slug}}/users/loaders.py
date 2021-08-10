from aiodataloader import DataLoader

from .models import User

__all__ = (
    "UserByIdLoader",
    "UserByUsernameLoader"
)


class UserByIdLoader(DataLoader):
    async def batch_load_fn(self, keys):
        users = User.objects.in_bulk(keys)
        return [users.get(id=user_id) for user_id in keys]


class UserByUsernameLoader(DataLoader):
    async def batch_load_fn(self, keys):
        users = User.objects.filter(username__in=keys)
        return [users.get(username=username) for username in keys]
