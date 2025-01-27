.PHONY: lint
lint:
	ruff format
	ruff check --fix
	ruff format

.PHONY: test
test:
	pytest
