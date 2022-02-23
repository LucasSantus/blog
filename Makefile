ENV = env
MANAGE = python manage.py

help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST); \

migrate: ## Migrate Models
	$(MANAGE) makemigrations home; \
	$(MANAGE) makemigrations blog; \
	$(MANAGE) makemigrations usuarios; \
	$(MANAGE) migrate; \

clear: ## Clean project
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@find . -name "env" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log

db-clear: ## Clean Database
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -rf db.sqlite3