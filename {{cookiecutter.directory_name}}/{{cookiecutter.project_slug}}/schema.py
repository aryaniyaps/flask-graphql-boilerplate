from graphene import relay, ObjectType, Schema

from {{ cookiecutter.project_slug }}.users.queries import UserQuery
from {{ cookiecutter.project_slug }}.users.mutations import UserMutation


class Query(
    UserQuery,
    ObjectType
):
    """
    this is the root `query` field for the
    GraphQL schema. This class must include
    every query as it's method.
    """
    
    # root node interface.
    node = relay.Node.Field()


class Mutation(
    UserMutation,
    ObjectType
):
    """
    this is the root `mutation` field for 
    the GraphQL schema. This class must include
    every mutation as it's method.
    """
    pass


schema = Schema(
    query=Query, 
    mutation=Mutation
)
