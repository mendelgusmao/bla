IMAGE:="bla/backend"

run: docker/build
	docker-compose up

destroy:
	docker-compose down

docker/build:
	docker build -t $(IMAGE) .

env/prepare:
	pip3 install poetry
	poetry install
	make qa/pre-commit/install

qa/pre-commit/install:
	poetry run pre-commit install

qa/lint:
	poetry run isort ./bla
	poetry run black --line-length=88 ./bla
	poetry run flake8 ./bla
	poetry run mypy ./bla

qa/test:
	poetry run pytest ./bla/tests

qa/test/coverage:
	poetry run coverage run -m pytest ./bla/tests
	poetry run coverage report --show-missing
