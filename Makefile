SOLUTION_DIR = src/aoc/solutions
README_FILE = README.md
INTRO_FILE = misc/readme-intro.md

build: 
	@uv sync --all-extras --dev && uv build

fmt: 
	@uvx ruff format

run-latest:
	@latest_file=$$(ls -1v $(SOLUTION_DIR)/*.py | tail -n 1); \
	if [ -n "$$latest_file" ]; then \
		day=$$(basename $$latest_file .py); \
		echo "# Computing solution - day $$day"; \
		python $$latest_file; \
	else \
		echo "No solution files found in $(SOLUTION_DIR)"; \
		exit 1; \
	fi

prun-latest:
	@make run-latest | glow

run-all:
	@for file in $(SOLUTION_DIR)/*.py; do \
		day=$$(basename $$file .py); \
		echo "# Computing solution - day $$day"; \
		python $$file; \
		echo ""; \
	done

prun-all:
	@make run-all | glow

readme:
	@cat $(INTRO_FILE) > $(README_FILE)
	@echo "## Solutions" >> $(README_FILE)
	@echo "| **Day** | **Solution** |" >> $(README_FILE)
	@echo "| --- | -------- |" >> $(README_FILE)
	@for file in $(SOLUTION_DIR)/*.py; do \
		day=$$(basename $$file .py); \
		echo "| $$day | [Link](./$$file) |" >> $(README_FILE); \
	done
	@echo "README.md generated successfully"

update: build fmt readme
	@git add . && git commit -m "Update"

new:
	@echo "Creating a new solution file..."
	@last_day=$$(ls -1v $(SOLUTION_DIR)/*.py 2>/dev/null | tail -n 1 | xargs -n 1 basename | sed 's/\.py//'); \
	next_day=$$((10#$${last_day:-0} + 1)); \
	new_file="$(SOLUTION_DIR)/$$(printf '%02d.py' $$next_day)"; \
	echo "Creating $$new_file"; \
	echo 'from aoc.utilities.fetch import get_input\n\ndata = get_input('$$next_day')' > $$new_file; \
	echo "New solution file $$new_file created successfully!"