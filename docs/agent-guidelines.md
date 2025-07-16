# Agentic AI Contribution Guidelines

This document outlines the rules and best practices for the AI pair-programmer (Cursor) contributing to the `alegator-backend` repository.

## 1. Core Principles

*   **Documentation-First:** Before writing code, ensure you understand the goal by consulting the `docs/` directory. Changes to the system's behavior must be reflected in the documentation *first*.
    *   `architecture.md`: For system-wide changes.
    *   `data-model.md`: For schema changes.
    *   `use-cases.md`: For new or modified features.
*   **Safety & Security:** Prioritize secure coding practices.
    *   NEVER commit secrets or PII.
    *   All database access MUST use the Django ORM. Raw SQL is forbidden.
    *   Validate and sanitize all user-provided data.
*   **Respect the Stack:** Adhere to the project's established technologies and patterns (Django, DRF, Celery, Supabase Auth). Do not introduce new dependencies without human approval.

## 2. Development Workflow

When implementing a feature or fixing a bug, the agent **MUST** follow these steps:

1.  **Acknowledge Task:** Confirm understanding of the goal, referencing the relevant use case (e.g., `UC-07`).
2.  **Update Documentation (if necessary):** Propose changes to the relevant Markdown files in `docs/`.
3.  **Write/Modify Code:**
    *   Implement the business logic in the appropriate Django app.
    *   Follow existing code style and patterns.
4.  **Write/Update Tests:**
    *   Add unit or integration tests under the relevant `app/tests/` directory.
    *   Ensure all tests pass.
5.  **Validate Schema:**
    *   If models were changed, run `python manage.py makemigrations --check --dry-run` to verify that migration files can be created without error.
6.  **Propose Pull Request:**
    *   NEVER push directly to the `main` branch.
    *   Open a Pull Request with a descriptive title (e.g., `feat: Implement UC-07 Break Generation`).
    *   The PR description must link to the relevant use case or issue.
    *   Request review from a human developer.

## 3. Human Interaction

*   Seek clarification when a request is ambiguous or conflicts with established architecture.
*   For destructive operations (e.g., irreversible schema changes), always require explicit human confirmation before proceeding. 