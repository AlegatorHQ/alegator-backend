# API Contract

This document defines the REST API contract for the Alegator platform. The API follows standard conventions for RESTful design.

## General Principles

### Versioning

All API endpoints are prefixed with a version number. The current version is `v1`.

Example: `https://api.alegator.com/api/v1/tournaments`

### Authentication

Endpoints that require authentication expect a JSON Web Token (JWT) to be passed in the `Authorization` header as a Bearer token.

`Authorization: Bearer <your_jwt_token>`

Endpoints that require authentication are marked as such.

### Error Responses

The API uses standard HTTP status codes to indicate the success or failure of a request. In case of an error (4xx or 5xx status codes), the response body will contain a JSON object with a standardized error format.

**Error Response Body:**
```json
{
  "timestamp": "2025-03-20T12:00:00Z",
  "status": 404,
  "error": "Not Found",
  "message": "Resource not found with id 123",
  "path": "/api/v1/tournaments/123"
}
```

### Pagination

For requests that return a list of resources, the API supports pagination via query parameters.

*   `page` (optional, default: 1): The page number to retrieve.
*   `size` (optional, default: 20): The number of items per page.

---

## Authentication and Users

### `POST /api/v1/auth/register`

*   **Description:** Creates a new user account.
*   **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "a_strong_password",
      "first_name": "John",
      "last_name": "Doe"
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe"
    }
    ```

### `POST /api/v1/auth/login`

*   **Description:** Authenticates a user and returns a JWT.
*   **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "a_strong_password"
    }
    ```
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

### `POST /api/v1/auth/logout`

*   **Description:** Logs out the user. Requires authentication.
*   **Request Body:**
    ```json
    {
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```
*   **Response Body (Success 204 - No Content):** (Empty)

### `GET /api/v1/users/me`

*   **Description:** Retrieves the profile of the currently authenticated user. Requires authentication.
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe"
    }
    ```

### `PATCH /api/v1/users/me`

*   **Description:** Allows the authenticated user to update their profile information. Requires authentication.
*   **Request Body:**
    ```json
    {
      "first_name": "Jane",
      "last_name": "Doer"
    }
    ```
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "first_name": "Jane",
      "last_name": "Doer"
    }
    ```

### `GET /api/v1/users/:id`
*   **Description:** Retrieves the public profile of a user by their ID.
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe"
    }
    ```

### `GET /api/v1/users/me/tournaments`
*   **Description:** Lists the tournaments the authenticated user is participating in or organizing. Requires authentication.
*   **Response Body (Success 200 - OK):**
    ```json
    [
        {
            "id": 1,
            "name": "Torneo Nacional de Debate",
            "role": "admin"
        }
    ]
    ```

---
## Tournament Management

### `GET /api/v1/tournaments`

*   **Description:** Lists all active public tournaments. Supports pagination.
*   **Response Body (Success 200 - OK):**
    ```json
    [
      {
        "id": 1,
        "name": "Torneo Nacional de Debate",
        "description_tournament": "El torneo anual de debate de Panamá.",
        "tournament_status": "active",
        "start_date": "2025-08-01",
        "end_date": "2025-08-03",
        "place": "Ciudad de Panamá"
      }
    ]
    ```

### `POST /api/v1/tournaments`

*   **Description:** Creates a new tournament. Requires authentication.
*   **Request Body:**
    ```json
    {
        "name": "Abierto de Debate de Panamá",
        "description_tournament": "Un nuevo torneo para todos.",
        "tournament_status": "upcoming",
        "avoid_same_institution": true,
        "shortname": "ADP2025",
        "place": "Ciudad de Panamá",
        "missing_feedbacks": false,
        "feedback_description": "",
        "minimum_panel_score": 70,
        "check_in": true,
        "start_date": "2025-09-10",
        "end_date": "2025-09-12"
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    {
        "id": 2,
        "name": "Abierto de Debate de Panamá",
        "description_tournament": "Un nuevo torneo para todos.",
        "tournament_status": "upcoming",
        "avoid_same_institution": true,
        "shortname": "ADP2025",
        "place": "Ciudad de Panamá",
        "missing_feedbacks": false,
        "feedback_description": "",
        "minimum_panel_score": 70,
        "check_in": true,
        "start_date": "2025-09-10",
        "end_date": "2025-09-12",
        "creator_id": 1
    }
    ```

### `GET /api/v1/tournaments/:id`

*   **Description:** Retrieves the full details of a specific tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    {
        "id": 1,
        "name": "Torneo Nacional de Debate 2025",
        "description_tournament": "El torneo anual de debate de Panamá.",
        "tournament_status": "active",
        "avoid_same_institution": true,
        "shortname": "TND2025",
        "place": "Ciudad de Panamá",
        "missing_feedbacks": true,
        "feedback_description": "La retroalimentación es obligatoria para todos los jueces.",
        "minimum_panel_score": 75,
        "check_in": true,
        "start_date": "2025-08-01",
        "end_date": "2025-08-03",
        "creator_id": 1
    }
    ```

### `PATCH /api/v1/tournaments/:id`

*   **Description:** Updates the general information of a tournament. Requires tournament admin role.
*   **Request Body:**
    ```json
    {
        "name": "Torneo Nacional de Debate 2025",
        "place": "Ciudad de Panamá"
    }
    ```
*   **Response Body (Success 200 - OK):** (Returns the updated tournament object, same as GET)

### `DELETE /api/v1/tournaments/:id`

*   **Description:** Deletes a tournament. Requires tournament admin role.
*   **Response Body (Success 204 - No Content):** (Empty)

### `POST /api/v1/tournaments/:id/register`

*   **Description:** Allows a user to register for a tournament. Requires authentication. This creates a `usertournament` record.
*   **Request Body:**
    ```json
    {
      "role": "participant"
    }
    ```
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "id": 1,
      "user_id": 1,
      "tournament_id": 1,
      "role": "participant"
    }
    ```

### `GET /api/v1/tournaments/:id/participants`

*   **Description:** Lists all participants (speakers, judges) of a tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    {
      "speakers": [
        { "id": 1, "name": "Speaker One", "province": "Panamá", "delegation": "Universidad de Panamá", "is_novice": false },
        { "id": 2, "name": "Speaker Two", "province": "Colón", "delegation": "Universidad del Istmo", "is_novice": true }
      ],
      "judges": [
        { "id": 1, "name": "Judge One", "province": "Chiriquí", "delegation": "Universidad Tecnológica de Panamá", "basescore": 4.5 }
      ]
    }
    ```

### `GET /api/v1/tournaments/:id/my-data`
*   **Description:** Shows the authenticated user's participation data in that tournament. Requires authentication.
*   **Response Body (Success 200 - OK):**
    ```json
    {
        "user_id": 1,
        "tournament_id": 1,
        "role": "participant",
        "speaker_profile": {
            "id": 1,
            "name": "Speaker One",
            "province": "Panamá",
            "delegation": "Universidad de Panamá",
            "is_novice": false
        },
        "judge_profile": null
    }
    ```

---

## Tournament Administration

Requires tournament admin role for all endpoints in this section.

### Rondas (Rounds)

#### `GET /api/v1/tournaments/:id/rounds`
*   **Description:** List all rounds for a tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    [
        {
            "id": 1,
            "tournament_id": 1,
            "name": "Round 1",
            "motion": "This house would ban tilapias.",
            "infoslide": "More additional information what no one really reads.",
            "round_number": 1,
            "round_status": "announced",
            "round_type": true,
            "is_silenced": false
        }
    ]
    ```

#### `POST /api/v1/tournaments/:id/rounds`
*   **Description:** Create a new round.
*   **Request Body:**
    ```json
    {
        "name": "Round 2",
        "motion": "This house believes that...",
        "infoslide": "",
        "round_number": 2,
        "round_status": "draft",
        "round_type": true,
        "is_silenced": true
    }
    ```
*   **Response Body (Success 201 - Created):** (Returns the newly created round object)

#### `PATCH /api/v1/tournaments/:id/rounds/:round_id`
*   **Description:** Updates a round.
*   **Request Body:**
    ```json
    {
        "motion": "A new motion.",
        "round_status": "announced"
    }
    ```
*   **Response Body (Success 200 - OK):** (Returns the updated round object)

#### `DELETE /api/v1/tournaments/:id/rounds/:round_id`
*   **Description:** Deletes a round.
*   **Response Body (Success 204 - No Content):** (Empty)

### Speakers

#### `GET /api/v1/tournaments/:id/speakers`
*   **Description:** Lists all speakers in the tournament.
*   **Response Body (Success 200 - OK):** (Array of speaker objects)
    ```json
    [
      { "id": 1, "user_id": 1, "name": "Speaker One", "province": "Panamá", "delegation": "Universidad de Panamá", "is_novice": false }
    ]
    ```

#### `POST /api/v1/tournaments/:id/speakers`
*   **Description:** Adds a new speaker to the tournament.
*   **Request Body:**
    ```json
    {
        "name": "Speaker Two",
        "province": "Colón",
        "delegation": "Universidad del Istmo",
        "is_novice": true,
        "user_id": 2
    }
    ```
*   **Response Body (Success 201 - Created):** (Returns the new speaker object)


### Jueces (Judges)

#### `GET /api/v1/tournaments/:id/judges`
*   **Description:** List all judges in the tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    [
        {
            "id": 1,
            "name": "Pedro Pedrez",
            "province": "Panamá",
            "delegation": "Colegio Nacional de Abogados",
            "team_id": 3,
            "basescore": 5.0
        }
    ]
    ```

#### `POST /api/v1/tournaments/:id/judges`
*   **Description:** Add a new judge to the tournament.
*   **Request Body:**
    ```json
    {
        "name": "Ines Perado",
        "province": "Coclé",
        "delegation": "Universidad Tecnológica de Panamá",
        "team_id": null,
        "basescore": 4.0
    }
    ```
*   **Response Body (Success 201 - Created):** (Returns the new judge object)


### Equipos (Teams)

#### `GET /api/v1/tournaments/:id/teams`
*   **Description:** List all teams in the tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    [
        {
            "id": 1,
            "name": "Team Alpha",
            "speaker_1_id": 1,
            "speaker_2_id": 2
        }
    ]
    ```

#### `POST /api/v1/tournaments/:id/teams`
*   **Description:** Create a new team.
*   **Request Body:**
    ```json
    {
        "name": "Team Beta",
        "speaker_1_id": 3,
        "speaker_2_id": 4
    }
    ```
*   **Response Body (Success 201 - Created):** (Returns the new team object)

### Draws y Sorteos (Draws and Pairings)

#### `POST /api/v1/tournaments/:id/draw`
*   **Description:** Generates the draw (pairings) for a specific round.
*   **Request Body:**
    ```json
    {
        "round_id": 1
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    [
        {
            "id": 1,
            "round_id": 1,
            "draw_status": "confirmed",
            "ag_id": 1,
            "ao_id": 2,
            "bg_id": 3,
            "bo_id": 4
        }
    ]
    ```

#### `GET /api/v1/tournaments/:id/draw/:round_id`
*   **Description:** Gets the draw for a specific round.
*   **Response Body (Success 200 - OK):** (Returns array of draw objects for the round)

#### `POST /api/v1/tournaments/:id/draw/:draw_id/judges`
*   **Description:** Assigns judges to a specific debate (draw).
*   **Request Body:**
    ```json
    {
        "judge_id": 1,
        "role": "chair"
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    {
        "id": 1,
        "draw_id": 1,
        "judge_id": 1,
        "role": "chair",
        "is_checked": false
    }
    ```

### Resultados (Results)

#### `POST /api/v1/tournaments/:id/results/teams`
*   **Description:** Register results for teams in a draw.
*   **Request Body:**
    ```json
    {
        "draw_id": 1,
        "results": [
            {"team_id": 1, "position": "AG", "points": 3},
            {"team_id": 2, "position": "AO", "points": 2},
            {"team_id": 3, "position": "BG", "points": 1},
            {"team_id": 4, "position": "BO", "points": 0}
        ]
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    {
        "message": "Team results registered successfully."
    }
    ```

### Feedbacks

#### `POST /api/v1/tournaments/:id/feedbacks`
*   **Description:** Submit feedback for a judge or speaker. Requires authentication.
*   **Request Body:**
    ```json
    {
        "draw_id": 1,
        "feedback_type": "speaker_to_judge",
        "given_by": "Speaker Name",
        "target": "Judge Name",
        "comment": "Very insightful feedback.",
        "score": 5
    }
    ```
*   **Response Body (Success 201 - Created):** (Returns the created feedback object)

---

## Roles and Security

Requires tournament admin role.

### `GET /api/v1/tournaments/:id/roles`
*   **Description:** Get a list of users and their roles in the tournament.
*   **Response Body (Success 200 - OK):**
    ```json
    [
        {"user_id": 1, "role": "admin"},
        {"user_id": 2, "role": "judge"},
        {"user_id": 3, "role": "participant"}
    ]
    ```

### `POST /api/v1/tournaments/:id/roles`
*   **Description:** Assign a role to a user in the tournament.
*   **Request Body:**
    ```json
    {
        "user_id": 4,
        "role": "participant"
    }
    ```
*   **Response Body (Success 201 - Created):**
    ```json
    {
        "id": 4,
        "user_id": 4,
        "tournament_id": 1,
        "role": "participant"
    }
    ```

### `DELETE /api/v1/tournaments/:id/roles/:user_id`
*   **Description:** Revokes a user's role in a tournament.
*   **Response Body (Success 204 - No Content):** (Empty)
