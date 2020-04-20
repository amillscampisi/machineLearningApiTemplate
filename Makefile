ROOT_DIR = ${PWD}
#PROJ_DIR =
#SRC_DIR =
#TEST_DIR =

export PYTHONPATH=$(ROOT_DIR)
export ENV_NAME=local

install:
	pipenv install --dev

run:
	pipenv run python application.py

test:
	pipenv run pytest $(TEST_DIR) --cov=$(PROJ_DIR) -v