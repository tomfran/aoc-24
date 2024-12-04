SOLUTION_DIR = src/aoc/solutions
README_FILE = README.md
INTRO_FILE = misc/readme-intro.md

build: 
	@uv sync --all-extras --dev && uv build

fmt: 
	@uvx ruff format

clean: 
	@uv clean

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

run-all:
	@for file in $(SOLUTION_DIR)/*.py; do \
		day=$$(basename $$file .py); \
		echo "# Computing solution - day $$day"; \
		python $$file; \
		echo ""; \
	done

readme:
	@cat $(INTRO_FILE) > $(README_FILE)
	@echo "## Solutions" >> $(README_FILE)
	@echo "| **Day** | **Link** | **Total Lines** | **Effective Lines** | **Last Updated** |" >> $(README_FILE)
	@echo "| -: | - | -: | -: | -: |" >> $(README_FILE)
	@for file in $(SOLUTION_DIR)/*.py; do \
		day=$$(basename $$file .py); \
		total_lines=$$(wc -l < $$file); \
		effective_lines=$$(grep -cve '^\s*$$' -e '^\s*#' $$file); \
		last_updated=$$(stat -f '%Sm' -t '%a, %b %d, %Y' $$file); \
		echo "| $$day | [Link](./$$file) | $$total_lines | $$effective_lines | $$last_updated |" >> $(README_FILE); \
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


# Pretty Run commands, need https://github.com/charmbracelet/glow

run:
	@make run-latest | glow

runa:
	@make run-all | glow