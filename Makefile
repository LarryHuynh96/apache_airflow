PYTHON = poetry run python
BLACK = poetry run black
PYLINT = poetry run pylint

SRC_DIR = dags/

format:
	$(BLACK) $(SRC_DIR)

lint:
	$(PYLINT) $(SRC_DIR)

install:
	poetry install

test:
	$(PYTHON) -m unittest discover

all: format lint

