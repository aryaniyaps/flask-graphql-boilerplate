from aiodataloader import DataLoader

from .models import User


class UserByIdLoader(DataLoader):
    """
    Loads users by their User-ID.
    """
    async def batch_load_fn(self, keys):
        user_map = User.objects.in_bulk(keys)
        return [user_map.get(user_id) for user_id in keys]


class UserByUsernameLoader(DataLoader):
    """
    Loads users by their username.
    """
    async def batch_load_fn(self, keys):
        users = User.objects(username__in=keys)
        user_map = {}
        for user in users:
            user_map[user.username] = user
        return [user_map.get(username) for username in keys]
