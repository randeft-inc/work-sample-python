# Randeft work sample

This work sample is based on a simplified reporting system that extracts data from a source, analyses it and writes the results on the local drive. It is a pure Python code sample, no other framework knowledge required. Python's unittest is used for tests, but prior knowledge is not a requirement: it should be straightforward to extend the existing tests.

## The Assignment

To evaluate not only how you code, but how you refactor to handle changing requirements, the assignement is split into two parts:

### Part 1

Our client, Materials Science Savvy Maestros, MSSM for short, is asking for a modification to their reporting system.

Please email "mssm.randeft@gmail.com" including a "[MSSM Start]" prefix in the subject line, and you will receive the requirements to get started.

### Part 2

After you submit part 1, MSSM will have some new requirements. Change your code as needed to implement them cleanly.

## Getting set up

### Prerequisites

The development environment is contained in a Docker Dev Container, so the only things needed on your machine are:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://docs.docker.com/desktop/release-notes/) (latest version)
- [Visual Studio Code](https://code.visualstudio.com/) (latest version)
- The Visual Studio Code [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

The setup will work on both Intel (amd64) and Apple Silicon (arm64) processors.

When opening the project in VSCode, the Dev Container extension should
prompt you to "**Reopen in Container**". Select that option to create
a Dev Container. This will take a few minutes the first time, and will
only take a few seconds the following times.

All following command are to be run in the VSCode integrated terminal,
after VSCode has been "reopened in Container".

### Anonymity Setup

To remove bias, the submissions will be made anonymously. To set up anonymity, in the VSCode terminal, run:

    ./scripts/anonymize.sh

This will set the Git name to a random string, and Git email to "<>", making all your commits anonymous. You can safely rerun the command when you need to consult your ID later (it will not regenerate a new ID if one has already been set).

### Dependency management

Defaults dependencies are automatically installed when the Dev Container is created. If you need to add more dependencies, you can do so by editing the `requirements.txt` file, and then running:

    pip install -r requirements.txt

### Unit tests

Verify that the unit tests run without errors with:

    make test

Note: for this work sample, we only use unit tests, no integration tests.

## Running the reporting system

To run the reporting system:

    make run

This will generate files in the `output` folder, from files in the `raw_data` folder.

## Repository submission

We will review not only your code but also your commits history. To allow this, please put all your commits on a branch named `feature/cloud_upload`, and bundle your local Git repository using the following command:

    (MSSM_ID=$(git config --local user.name) && git bundle create mssm-${MSSM_ID}.repo --all)

You can then right-click on the created `.repo` file in VS Code and select "Download..." to copy the file from the Docker container to your local machine.

## Work sample review

Your work sample will be evaluated using various criteria. We will pay particular attention to:

- Thoroughness and attention to detail
- Ability to follow instructions
- Consistency with the existing codebase
- Readability and maintainability

## Important Notes

- You can and should review the existing codebase, search the Web for solutions, use libraries, etc...
- Each part of this work sample should take 2 to 4 hours, but there is no time limit, you can take as long as you need.
- Feel free to withdraw your application if it is taking you longer that you are willing to commit, no hard feelings or impact on further applications.
- We are looking for any feedback about this work sample itself. Please let us know what you thought about it.
