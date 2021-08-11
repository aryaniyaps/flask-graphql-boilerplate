<p align="center">
  <img src="assets/banner.jpg" />
  a Flask template for <a href="https://github.com/cookiecutter/cookiecutter">cookiecutter</a> to get you up and running, powered by GraphQL.
</p>

## Motivation ⛵

The GraphQL community is relatively new, and there are fewer resources to help you get started with it in the Python ecosystem. While I started to write
GraphQL projects with Python, I experienced a lot of friction, and wrote a lot of boilerplate code. Eventually, I figured out that it would be easier to
make a template which would help me to get up and running. This template uses a lot of modern libraries to provide the best developer experience. Today, I
mostly start off my projects with this template.

## Features at a glance ✨

- [x] Built for [Flask](https://github.com/pallets/flask) 2.0.1
- [x] Works with Python 3.8
- [x] Uses [Graphene](https://github.com/graphql-python/graphene) for the GraphQL schema.
- [x] Pre-Configured [Jinja2](https://github.com/pallets/jinja) email templates.
- [x] Built in support for sending emails.
- [x] [MongoEngine](https://github.com/MongoEngine/mongoengine) ODM support.
- [x] Uses [Pipenv](https://github.com/pypa/pipenv) to manage dependencies.
- [x] Comes with support for [Flask-CORS](https://github.com/corydolphin/flask-cors).
- [x] Offers complete support for the [Relay](https://github.com/facebook/relay) API spec.
- [x] GraphQL file uploads support.
- [x] Batch querying support (for use with [Apollo Client](https://github.com/apollographql/apollo-client)).
- [x] Follows the official [Shopify GraphQL Design](https://github.com/Shopify/graphql-design-tutorial) guide.
- [x] Uses [Pytest](https://github.com/pytest-dev/pytest) and [FactoryBoy](https://github.com/FactoryBoy/factory_boy) for testing.
- [x] [DataLoader](https://github.com/syrusakbary/aiodataloader) support (fixes the n+1 problem).
- [ ] Uses [Cerberus](https://github.com/pyeve/cerberus) for input validation.
- [ ] Comes with an authentication system which handles:
  - [ ] User email confirmation.
  - [ ] Forgot password/ password reset.
  - [ ] Verified email/ password changes.
  - [x] User creation/ login.
  - [x] User authentication with [Flask-Login](https://github.com/maxcountryman/flask-login).
  - [x] Storing passwords with [Argon2](https://github.com/hynek/argon2-cffi).

## Using the boilerplate 🚀

using the boilerplate is very simple! Make sure that you have pip installed.
If you don't have cookiecutter already, use the following command.

```cmd
pip install cookiecutter
```

You can get started by entering the following command.

```cmd
cookiecutter https://github.com/codebyaryan/flask-graphql-boilerplate
```

## Contributing 📄

This project is open for contributions! Make sure to read the [contributing guidelines](.github/CONTRIBUTING.md) to get started.
