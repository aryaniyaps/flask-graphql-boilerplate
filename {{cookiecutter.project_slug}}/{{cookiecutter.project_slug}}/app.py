from datetime import datetime

from flask import Flask

from {{ cookiecutter.project_slug }} import extensions
from {{ cookiecutter.project_slug }} import users


from strawberry.flask.views import GraphQLView


def create_app(config="{{ cookiecutter.project_slug }}.settings"):
    app = Flask(__name__)
    app.config.from_object(config)

    app.add_url_rule(
        rule="/graphql",
        view_func=GraphQLView.as_view(
            name="graphql",
            schema=schema,
            graphiql=app.config.get("DEBUG")
        )
    )

    register_extensions(app)
    register_context_processors(app)
    register_shell_context(app)
    return app


def register_extensions(app):
    """
    registers extensions for the server.
    """
    extensions.mail.init_app(app)
    extensions.db.init_app(app)
    extensions.bcrypt.init_app(app)


def register_shell_context(app):
    """
    registers the shell context for the server.
    """

    def shell_context():
        return {
            'db': extensions.db,
            'User': users.models.User
        }

    app.shell_context_processor(shell_context)


def register_context_processors(app):
    """
    registers context processors which
    inject values into templates.
    """

    def inject_now():
        """
        returns the current UTC
        date-time instance.
        """
        return {"now": datetime.utcnow()}

    app.context_processor(inject_now)
