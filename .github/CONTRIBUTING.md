## Our Development Process

All changes happen through pull requests. Pull requests are the best way to propose changes.
We actively welcome your pull requests and invite you to submit pull requests directly
[here](https://github.com/codebyaryan/flask-graphql-boilerplate/pulls), and after review, these can be merged into the project.

## Developer notes

The boilerplate must not be very opinionated. It should provide a basic set of features
which must be easily extensible.

When it comes to mutations, we always prefer to use `ClientIDMutation` subclassess instead of `Mutation` subclasses because
this gives the server and client more control over features like caching and preventing duplication.

## Testing the boilerplate

We are planning to use pytest in order to test the boilerplate. Tests haven't been setup yet,
but this section will contain information on how to run them after they are completed.

## Pull Requests

1. Fork the repo and create your branch (usually named `patch-%the number of PRs you've already made%`).
2. If you've added code that should be tested, add some test examples.
3. Ensure to describe your pull request.

## Feature Request

Great Feature Requests tend to have:

- A quick idea summary.
- What & why you wanted to add the specific feature.
- Additional context like images, links to resources to implement the feature etc, etc.

## License

By contributing to this project, you agree that your contributions will be licensed
under the [LICENSE file](../LICENSE).
