# Style Guide

This project follows the
[Airbnb JavaScript Style Guide](https://airbnb.io/javascript/), but there is no
need to know the whole thing: the editor's linter will help you.

There is one modification:

- Maximum line length is 80 characters.


# Naming Rules

> Any fool can write code that a computer can understand. Good programmers write
> code that humans can understand.
>
> -- <cite>Martin Fowler</cite>

Naming is hard. Precise, expressive, and intention-revealing naming is very
important for readability, so make sure you choose good variable and method
names.

Use American english (e.g.: `color`, not `colour`), and the ASCII charset.


# Git Commit Messages

As with naming, good commit messages are important: they provide context to
other humans when reviewing code changes.

We follow [these recommendations](https://cbea.ms/git-commit/) when writing Git
commit messages:

1. Separate subject from body with a blank line.
2. Limit the subject line to 50 characters.
3. Capitalize the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood in the subject line.
6. Wrap the body at 72 characters.
7. Use the body to explain what and why, not how (how is the code, and the code
  should be self-explanatory).


# Git Commit History

A good commit history can greatly facilitate code reviews: it gives context to
the evolution of the code and shows the various steps of the implementation. So
be sure to clean up your git history before submitting:

- Do not leave "WIP" commits behind.
- Squash fixup commits with the commit they fix.
- But keep separate commits for the separate steps of your implementation.
- Try to have tests pass for every commit (this facilitates git bisect).

Exemple of a **bad** commit history:

    | * Fix tests
    | * Finish upload
    | * Fix typo
    | * Refactor
    | * WIP Implement upload
    | * Commit forgotten package-lock.json
    | * Add node-ftp package
    |/
    *

Exemple of a **good** commit history:

    | * Add FTP uploader to processing pipeline
    | * Implement FTP uploader
    | * Add node-ftp package
    | * Refactor to allow the use of multiple uploaders
    |/
    *
