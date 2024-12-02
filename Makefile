build: 
	uv sync --all-extras --dev && uv build

fmt: 
	uvx ruff format

all: build fmt
