# Api endpoints

## Autenticación y Usuarios

POST /api/auth/register
Descripción: Crear endpoint de registro con validación de rol y hash de contraseña.

POST /api/auth/login
Descripción: Crear endpoint de login que devuelva un token JWT válido.

POST /api/auth/logout
Descripción: Implementar logout del usuario y revocación del token (opcional: blacklist).

POST /api/auth/reset-password
Descripción: Crear lógica para recuperación de contraseña vía email con token temporal.

GET /api/users/me
Descripción: Obtener perfil del usuario autenticado.

PATCH /api/users/me
Descripción: Permitir al usuario editar su información personal.

GET /api/users/:id
Descripción: Obtener perfil público de un usuario por ID.

## Gestión de Torneos

GET /api/tournaments
Descripción: Listar torneos públicos activos.

GET /api/tournaments/:id
Descripción: Obtener detalles completos de un torneo (nombre, descripción, fechas, tipo).

POST /api/tournaments
Descripción: Crear un nuevo torneo, disparar la creación del nuevo schema UUID en la base de datos.

PATCH /api/tournaments/:id
Descripción: Editar los datos generales de un torneo.

DELETE /api/tournaments/:id
Descripción: Eliminar torneo y, si aplica, su schema completo.

POST /api/tournaments/:id/register
Descripción: Permitir a un usuario inscribirse en el torneo con validación de rol.

GET /api/tournaments/:id/participants
Descripción: Listar todos los participantes del torneo (oradores, jueces).

GET /api/tournaments/:id/my-data
Descripción: Mostrar al usuario sus propios datos de participación en ese torneo.

GET /api/users/me/tournaments
Descripción: Listar torneos donde el usuario participa o es organizador.

🧱 Migración: user_torneo_rol
Descripción: Crear tabla que relacione usuarios con torneos y sus roles (admin, juez, participante).

## Administración de Torneos

### 🔁 Rounds

GET /api/tournaments/:id/rounds: Listar todas las rondas.

POST /api/tournaments/:id/rounds: Crear nueva ronda.

PATCH /api/tournaments/:id/rounds/:round_id: Editar ronda.

DELETE /api/tournaments/:id/rounds/:round_id: Eliminar ronda.

### 👥 Teams y Speakers

GET /api/tournaments/:id/teams: Listar equipos del torneo.

POST /api/tournaments/:id/teams: Crear nuevo equipo.

PATCH /api/tournaments/:id/teams/:team_id: Editar equipo.

DELETE /api/tournaments/:id/teams/:team_id: Eliminar equipo.

GET /api/tournaments/:id/speakers: Listar oradores del torneo.

POST /api/tournaments/:id/speakers: Registrar orador.

PATCH /api/tournaments/:id/speakers/:speaker_id: Editar orador.

DELETE /api/tournaments/:id/speakers/:speaker_id: Eliminar orador.

### 🧑‍⚖️ Judges

GET /api/tournaments/:id/judges: Listar jueces.

POST /api/tournaments/:id/judges: Crear juez.

PATCH /api/tournaments/:id/judges/:judge_id: Editar juez.

DELETE /api/tournaments/:id/judges/:judge_id: Eliminar juez.

### 🎲 Draws y Sorteos

POST /api/tournaments/:id/draw: Crear draw (sorteo de equipos).

GET /api/tournaments/:id/draw/:round_id: Obtener draw de la ronda.

POST /api/tournaments/:id/draw/:draw_id/judges: Asignar jueces a un draw.

### 🏁 Resultados

POST /api/tournaments/:id/results/teams: Registrar resultados de equipos.

POST /api/tournaments/:id/results/speakers: Registrar resultados de oradores.

GET /api/tournaments/:id/results: Ver resultados generales del torneo.

### 🧾 Feedbacks

POST /api/tournaments/:id/feedbacks: Enviar feedback a juez u orador.

GET /api/tournaments/:id/feedbacks: Consultar feedbacks de la ronda/torneo.

### 📍 Check-in

POST /api/tournaments/:id/check-in/:round_id: Marcar asistencia de un participante o juez.

### 🏆 Break y Clasificación

POST /api/tournaments/:id/break: Generar fase de eliminación.

GET /api/tournaments/:id/break: Ver fase eliminatoria actual.

GET /api/tournaments/:id/standings: Obtener ranking general por puntaje.

## Roles y Seguridad

GET /api/tournaments/:id/roles
Descripción: Obtener lista de usuarios y sus roles en el torneo.

POST /api/tournaments/:id/roles
Descripción: Asignar rol a un usuario específico dentro del torneo.

DELETE /api/tournaments/:id/roles/:user_id
Descripción: Revocar rol de usuario en el torneo.

🧩 Middleware por torneo
Descripción: Crear middleware que verifique que el usuario tiene rol válido para acceder al torneo.