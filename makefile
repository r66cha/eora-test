docker-build:
	docker compose up --build -d


freeze:
	uv pip freeze > requirements.txt


install:
	uv pip install -r requirements.txt

parse:
	uv run python -m src.core.parser.parser

run:
	uv run main.py


build:
	docker compose up --build -d

run-all:
	pip install -r requirements.txt
	python3 main.py
