# WebSocket Event Contract

This document defines the schema for real-time events sent over Django Channels.

*   **Direction:** C→S (Client-to-Server) or S→C (Server-to-Client Broadcast).
*   **Channels:** Clients connect to a multiplexed stream and subscribe to specific channels.

| Channel Name         | Direction | Payload (JSON)                                               | Trigger                                                                |
|----------------------|-----------|--------------------------------------------------------------|------------------------------------------------------------------------|
| `draws:new`          | S → C     | `{"round_id": 1, "tournament_id": 1}`                        | Fired after the `generate_draw` background task completes successfully. Notifies clients that a new draw is available via the REST API. |
| `rounds:live`        | S → C     | `{"round_id": 1, "motion": "This house would..."}`           | Fired when an admin publishes a round, revealing the motion.          |
| `checkins:update`    | C → S     | `{"round_id": 1, "user_id": "uuid", "status": true}`         | Sent by a participant to mark themselves as present for a round.       |
| `checkins:status`    | S → C     | `{"round_id": 1, "user_id": "uuid", "status": true}`         | Broadcast by the server after a successful check-in to update all connected clients (especially admins). |
| `timers:sync`        | S → C     | `{"round_id": 1, "seconds_remaining": 420}`                  | Periodically broadcast by the server (e.g., every 5s) for an active round to keep timers synchronized across clients. |
| `standings:update`   | S → C     | `{"tournament_id": 1, "url": "/api/tournaments/1/standings"}` | Fired after the `recalc_standings` task completes. Informs clients that new rankings are available at the specified API endpoint. |

**Handshake**: Client includes `Sec-WebSocket-Protocol: jwt` header with Supabase JWT. Connection is rejected if invalid or expired. 