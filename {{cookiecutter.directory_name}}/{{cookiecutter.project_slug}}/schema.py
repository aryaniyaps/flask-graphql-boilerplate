import graphene

from {{ cookiecutter.project_slug }}.users.queries import UserQuery
from {{ cookiecutter.project_slug }}.users.mutations import UserMutation


class Query(
    UserQuery,
    graphene.ObjectType
):
    """
    this is the root `query` field for the
    GraphQL schema. This class must include
    every query as it's method.
    """
    pass


class Mutation(
    UserMutation,
    graphene.ObjectType
):
    """
    this is the root `mutation` field for 
    the GraphQL schema. This class must include
    every mutation as it's method.
    """
    pass


schema = graphene.Schema(
    query=Query, 
    mutation=Mutation
)
