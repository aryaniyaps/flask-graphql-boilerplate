import strawberry

from {{ cookiecutter.project_slug }}.users.queries import Query


schema = strawberry.Schema(query=Query)
