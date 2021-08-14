# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setting up your project

The first thing you need to do is install dependencies (via the following command).

```cmd
pipenv install
```

You also need to set the environment variables. Make sure to place it inside a `.env` file at the root level.
Look at the [example file](.env.example) for reference.

To setup the database with initial migrations (using alembic), run the following commands. You need to install 
PostgreSQL on your machine before that.

```cmd
flask db init
flask db migrate
flask db upgrade
```

## running the project

to run the project, use the following command.

```cmd
flask run
```

## Using the shell

to open the interactive shell locally, use the following command.

```cmd
flask shell
```

## Migrations
Whenever a database migration needs to be made, run the following commands.
```cmd
flask db migrate
```
This will generate a new migration script. Then run
```cmd
flask db upgrade
```
to apply the migration.

## Running tests

to run the test suite for the project, use the following command.

```cmd
flask test
```
