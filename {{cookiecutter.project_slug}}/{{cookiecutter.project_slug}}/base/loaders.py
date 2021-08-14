from aiodataloader import DataLoader
from flask import Request


class BaseLoader(DataLoader):
    """
    A generic data-loader which is initialized
    only once per request-cycle.
    """
    context = None
    context_key = None

    def __new__(cls, context: Request):
        if cls.context_key is None:
            raise TypeError("Data loader %r does not define a context key" % (cls,))
        if not hasattr(context, "loaders"):
            context.loaders = {}
        if cls.context_key not in context.loaders:
            setattr(
                context.loaders,
                cls.context_key,
                super().__new__(cls, context)
            )
        loader = context.loaders.get(cls.context_key)
        assert isinstance(loader, cls)
        return loader

    def __init__(self, context):
        if self.context == context:
            return
        self.context = context
        super().__init__()
