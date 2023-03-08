SHELL := /bin/bash

init:
	python -m venv venv

activate: venv
	source ./venv/bin/activate

clean:
	rm -rf dist

build: clean activate venv
	python -m build

dependency: venv
	pip install --upgrade pip twine build

upload: venv dist
	python -m twine upload --repository testpypi dist/*
