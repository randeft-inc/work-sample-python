# Randeft work sample

This work sample is based on a simplified reporting system that extracts data from a source, analyses it and writes the results on the local drive. It is a pure Javascript code sample, no other framework knowledge required. Jest is used for tests, but prior knowledge of Jest is not a requirement: it should be straightforward to extend the existing tests.

## The Assignment

To evaluate not only how you code, but how you refactor to handle changing requirements, the assignement is split into two parts:

### Part 1

Our client, Materials Science Savvy Maestros, MSSM for short, is asking for a modification to their reporting system.

Please email "mssm.randeft@gmail.com" including a "[MSSM Start]" prefix in the subject line, and you will receive the requirements to get started.

### Part 2

After you submit part 1, MSSM will have some new requirements. Change your code as needed to implement them cleanly.

## Getting set up

### Prerequisites

The development environment is contained in a Docker Dev Environment, so the only things needed on your machine are:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://docs.docker.com/desktop/release-notes/) (latest version)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code Remote Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

The setup will work on both Intel (amd64) and Apple Silicon (arm64) processors.

### Create the Dev Environment

Once you have the prerequisites installed, create a new Docker Dev Environment using this repo's cloning URL.

If you a unsure how to proceed, please follow the [Create a Dev Environment From a Git Repository](https://docs.docker.com/desktop/dev-environments/create-dev-env/#create-a-dev-environment-from-a-git-repository) instructions. Don't forget to replace the repo URL in the instructions with the URL for this repo.

Once the Dev Environment is started, click "Open in VSCode". A "Starting Dev Container" message will appear at the bottom right. Wait a few seconds until it dissapears, and you should be ready to start.

Open a terminal in VSCode. This will open a shell inside the Dev Environment container, and you should see a prompt like the following:

    node ➜ /com.docker.devenvironments.code (main) $

All following `npm` and other commands are to be run inside that Dev Environment shell.

#### Note about the Dev Environment lifecycle

Local changes you make in VSCode are persisted in a Docker volume. It is therefore safe to stop and restart the Dev Environment container: your changes, uncommitted code included, will still be there. But do not **delete** the dev environment: your changes would be lost.

### Anonymity Setup

To remove bias, the submissions will be made anonymously. To set up anonymity, in the VSCode terminal, run:

    ./scripts/anonymize.sh

This will set the Git name to a random string, and Git email to "<>", making all your commits anonymous. You can safely rerun the command when you need to consult your ID later (it will not regenerate a new ID if one has already been set).

### Dependency management

To install the dependencies, execute the following inside the repo's top-level folder:

    npm install

### Unit tests

Verify that the unit tests run without errors with:

    npm test unit

Note: for this work sample, we only use unit tests, no integration tests.

## Running the reporting system

To run the reporting system:

    npm start

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
