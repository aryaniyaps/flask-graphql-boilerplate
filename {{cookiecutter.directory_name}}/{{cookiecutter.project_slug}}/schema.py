import strawberry

from {{ cookiecutter.project_slug }}.users.queries import UserQuery
from {{ cookiecutter.project_slug }}.users.mutations import UserMutation


@strawberry.type
class Query(UserQuery):
    """
    this is the root `query` field for the
    GraphQL schema. This class must subclass
    all other Query classes.
    """
    pass


@strawberry.type
class Mutation(UserMutation):
    """
    this is the root `mutation` field for the
    GraphQL schema. This class must subclass
    all other Mutation classes.
    """
    pass


schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation
)
