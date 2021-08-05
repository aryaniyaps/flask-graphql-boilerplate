# {{ cookiecutter.project_name }} {{ cookiecutter.version }}

{{ cookiecutter.project_description }}

## Setting up your project

The first thing you need to do is install dependencies (via the following command).

```cmd
pipenv install
```

You also need to set the environment variables. Make sure to place it inside a `.env` file at the root level.
Look at the [example file](.env.example) for reference.

## Using the shell

to open the interactive shell locally, run the following command.

```cmd
flask shell
```

## Running tests

to run the test suite for the project, run the following command.

```cmd
flask test
```
