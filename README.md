<p align="center">
  <img src="assets/banner.jpg" />
  a Flask template for <a href="https://github.com/cookiecutter/cookiecutter">cookiecutter</a> to get you up and running, powered by GraphQL.
</p>

## Motivation

The GraphQL community is relatively new, and there are fewer resources to help you get started with it in the Python ecosystem. While I started to write
GraphQL projects with Python, I experienced a lot of friction, and wrote a lot of boilerplate code. Eventually, I figured out that it would be easier to
make a template which would help me to get up and running. This template uses a lot of modern libraries to provide the best developer experience. Today, I
mostly start off my projects with this template.

## Features at a glance

- [x] Built for [Flask](https://github.com/pallets/flask) 2.0.1
- [x] Works with Python 3.8
- [x] Uses [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry).
- [x] Pre-Configured [Jinja2](https://github.com/pallets/jinja) email templates.
- [x] [Mongoengine](https://github.com/MongoEngine/mongoengine) ODM support.
- [x] Uses [Pipenv](https://github.com/pypa/pipenv) to manage dependencies.
- [ ] GraphQL file uploads support.
- [ ] Uses [Pytest](https://github.com/pytest-dev/pytest) and [Factory-boy](https://github.com/FactoryBoy/factory_boy) for testing.
- [ ] Comes with an authentication system out of the box.
- [ ] optimized for Single Page Applications.

## Using the boilerplate

using the boilerplate is very simple! Make sure that you have cookiecutter installed.

```cmd
pip install cookiecutter
```

Once that's done, you can get started by entering the following command.
You'll be asked to enter the project variables.

```cmd
cookiecutter gh:codebyaryan/flask-graphql-boilerplate
```

However, if you don't want to provide any project variables, and want to stick with
the defaults, you can use this command instead.

```cmd
cookiecutter gh:codebyaryan/flask-graphql-boilerplate --noinput
```

## Contributing

This project is open for contributions! Make sure to read the [contributing guidelines](.github/CONTRIBUTING.md) to get started.
