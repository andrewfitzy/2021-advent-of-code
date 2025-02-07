.PHONY: init black ruff isort test lint compile-dependencies compile-regular-dependencies compile-dev-dependencies

init:
	@python -c 'import sys; assert sys.version_info >= (3, 10) and sys.version_info < (3, 11), "Python version must be 3.10"'
	@echo "Initializing virtual environment in .venv"
	@if [ ! -d ".venv" ]; then python -m venv .venv; fi
	@echo "Installing dependencies"
	@source .venv/bin/activate; pip install -qr requirements-dev.txt
	@echo "Installing pre-commit"
	@source .venv/bin/activate; pre-commit install
	@echo "Please run 'source .venv/bin/activate' to activate the virtual environment"

black:
	@black src/ tests/

ruff:
	@ruff src/ tests/

isort:
	@isort src/ tests/

test:
	pytest --cov-fail-under=80 --cov=src/ --cov-report=term-missing --cov-report=xml

test-file:
	TEST_ENV=local pytest $(file)

compile-regular-dependencies:
	@pip-compile --allow-unsafe --no-emit-index-url --resolver=backtracking requirements.in

compile-dev-dependencies:
	@pip-compile --allow-unsafe --no-emit-index-url --resolver=backtracking requirements-dev.in

lint: black ruff isort
compile-dependencies: compile-regular-dependencies compile-dev-dependencies
