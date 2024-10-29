# Makefile for the project

CHECK_TARGETS := $(shell grep -E '^check-' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":"} { print $$1 }')

.DEFAULT_GOAL := help
.PHONY: help test run $(CHECK_TARGETS)

help: ## Run `make help` to get help on the make commands
	@echo "\033[36mAvailable commands:\033[0m"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

check: ## Check all requirements  <-----  👉 START HERE 👈
check: $(CHECK_TARGETS)
	@echo '🎉 All checks have passed.'
	@echo 'You can now 👉 `make open` 👈 to open the project in VS Code.'
	@echo 'When prompted, select to `Reopen in Container`.'

check-not-dev-container:
	@test -z "$$REMOTE_CONTAINERS" || ( echo ❌ ERROR: Running inside a Dev Container. Please ensure this command is run outside of a Dev Container.; false )
	@echo '✅ Running outside a Dev Container'

check-docker-installed:
	@which docker >/dev/null || ( echo ❌ ERROR: Docker is not installed. Please install Docker from https://www.docker.com/products/docker-desktop/; false )
	@echo '✅ Docker is installed'

check-docker-running:
	@docker info >/dev/null 2>&1 || ( echo ❌ ERROR: Docker is not running. Please start Docker.; false )
	@echo '✅ Docker is running'

check-vscode-installed:
	@which code >/dev/null || ( echo ❌ ERROR: VS Code CLI command 'code' not found. Execute \`Shell Command: Install 'code' command in PATH\` in the VS Code Command Palette.; false )
	@echo '✅ VS Code CLI command is available'

check-dev-container-extension:
	@code --list-extensions | grep -q 'ms-vscode-remote.remote-containers' || ( echo ❌ ERROR: Dev Container VS Code extension is not installed. Please install it from the VS Code extensions marketplace.; false )
	@echo '✅ Dev Container VS Code extension is installed'

open: ## Open the project in VS Code
open: check-not-dev-container
	@code .
	@echo 'Opening the project in VS Code...'
	@echo 'When prompted, select to 👉 `Reopen in Container` 👈.'
	@echo
	@echo 'Once the Dev Container is built (it may take a few minutes),'
	@echo 'run 👉 `make test` 👈 to run the tests.'

test: ## Run the tests (inside the Dev Container)
test: in-dev-container
	@python -m unittest discover -p '*_test.py'

run: ## Run the application (inside the Dev Container)
run: in-dev-container
	@python -m app.app
	@echo '🎉 The application ran successfully.'

in-dev-container:
	@test -n "$$REMOTE_CONTAINERS" || ( echo ❌ ERROR: Running outside a Dev Container. Please ensure this command is run inside a Dev Container.; false )
	@echo '✅ Running inside a Dev Container'
