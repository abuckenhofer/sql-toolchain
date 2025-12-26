# SQL Toolchain Template

This repository is a starter template for writing and delivering clean, consistent, and reviewable SQL with automated quality checks.

**What’s inside**

SQLFluff linting & formatting to enforce a consistent SQL style (local CLI + CI)

Example configuration (.sqlfluff) and project conventions (SQL as “policy as code”)

A minimal demo setup you can copy into your own repositories

**How to use**

Create a new repo from this template (or fork it).

Adjust the SQLFluff configuration to your dialect and team conventions.

Install Python, create a virtual environment and setup the project:
```
python -m pip install -e .
```

Linting recursively a directory (default are *.sql files):
```
python -m sqlfluff lint src
```

Fixing recursively a directory:
```
python -m sqlfluff fix src
```

The directory sqlfluff_rules contains an example for an individual rule (sql-files requiring a comment at the beginning)

.github/workflows/sqlfluff.yml contains automation for github pushes. The file sqlfluff-annotations.json contains the violations.

Or even better use a pre-commit hook.
```
pip install pre-commit
pre-commit install
```
The file .pre-commit-config.yaml contains the configuration. Check manually:
```
pre-commit run --all-files
```
or alternatively git commit performs linting automatically.

**Roadmap**

Planned integrations include Liquibase for database change management and migrations, plus additional checks to support SQL documentation and governance.

**License**

Use it freely in your projects; attribution is appreciated.
