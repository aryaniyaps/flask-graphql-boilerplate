from graphene import relay, Schema

from {{ cookiecutter.project_slug }}.users.queries import UserQuery
from {{ cookiecutter.project_slug }}.users.mutations import UserMutation


__all__ = (
    "schema",
)


class Query(UserQuery):    
    # root node field definition.
    node = relay.Node.Field()


class Mutation(UserMutation):
    pass


schema = Schema(
    query=Query, 
    mutation=Mutation
)
