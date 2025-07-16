# Celery Task Catalogue

This document lists the asynchronous background tasks managed by Celery.

## 1. Task Design Principles

*   **Idempotency:** All tasks must be idempotent. Executing a task multiple times with the same input should produce the same result without unintended side effects.
*   **Transactional:** Where possible, tasks should use database transactions (`transaction.atomic`) to ensure data consistency.
*   **Locking:** To prevent race conditions on tournament-wide operations, tasks should acquire a distributed lock (e.g., via Redis) using the `tournament_id` as the lock key before execution.
*   **Failure & Retries:** Tasks are configured with a default retry policy. For critical tasks like standings calculation, an infinite retry policy with exponential backoff is used.

## 2. Task Definitions

| Task Signature                      | Trigger / Caller                      | Key Inputs      | Side Effects & Outputs                                                                                                      |
|-------------------------------------|---------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `generate_draw(round_id)`           | Admin action via `POST /rounds/{id}/draw` | `round_id`      | 1. Runs the British Parliamentary draw algorithm.<br>2. Populates the `draws` table for the given round.<br>3. Fires the `draws:new` WebSocket event. |
| `recalc_standings(tournament_id)`   | Ballot submission (`POST /ballots`)     | `tournament_id` | 1. Aggregates all ballot data.<br>2. Updates cached tables for team and speaker rankings.<br>3. Fires the `standings:update` WebSocket event. |
| `generate_break(tournament_id)`     | Admin action via `POST /tournaments/{id}/break` | `tournament_id` | 1. Calculates breaking teams based on standings.<br>2. Creates new `rounds` records with `type="break"`.<br>3. Can trigger a notification to admins. | 