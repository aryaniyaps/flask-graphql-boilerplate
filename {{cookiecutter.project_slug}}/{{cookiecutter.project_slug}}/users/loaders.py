from aiodataloader import DataLoader

from .models import User


class UserLoader(DataLoader):
    async def batch_load_fn(self, keys):
        return [User.objects(id=user_id).first() for user_id in keys]
