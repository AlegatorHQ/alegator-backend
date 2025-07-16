### Descripción General:
Este proyecto consiste en el desarrollo de una plataforma web que permita gestionar y
participar en torneos académicos, deportivos o de debate. Incluye funcionalidades para
usuarios generales (autenticación, inscripción, perfil y seguimiento de participación), así
como un robusto panel de administración para los organizadores del torneo, quienes
podrán configurar rondas, registrar resultados, generar clasificaciones, manejar listas de
participantes y administrar otros administradores.
El objetivo es digitalizar todo el proceso de inscripción, gestión y seguimiento de torneos,
facilitando la organización y mejorando la experiencia de participantes y jueces.

### Objetivos del Proyecto:
• Permitir a los usuarios registrarse, ver eventos, e inscribirse a torneos.
• Permitir a los administradores configurar y gestionar torneos complejos.
• Mantener un sistema de clasificación de oradores, equipos y rondas.
• Facilitar la visualización de resultados y feedbacks.
• Diseñar una interfaz clara y eficiente para participantes y organizadores.

### Características Funcionales Requeridas:
#### Funcionalidades Generales:
    1. Autenticación de Usuarios:
        - Registro, inicio de sesión y cierre de sesión.
        - Recuperación de contraseña.
    2. Perfil de Usuario:
        - Información básica (nombre, correo, rol: participante/juez/admin).
        -  Historial de torneos inscritos y organizados.
    3. Página de Inicio:
        - Introducción a la plataforma.
        - Acceso rápido a eventos, próximos torneos y perfil.
    4. Página de Eventos y Torneos:
        - Listado de torneos destacados e importantes.
        - Lista de próximos torneos disponibles.
        - Opción para inscribirse a los próximos torneos.
        - Redirección a sitios externos de torneos (si aplica).
        - Página "Mis Torneos": torneos inscritos, torneos organizados.

#### Módulo de Administración del Torneo (Tournament - Admin side):
• Crear y configurar un torneo (nombre, fechas, descripción, tipo, etc.).
• Gestionar rondas del torneo.
• Clasificación en tiempo real de equipos y oradores.
• Generar y editar el break (fase eliminatoria).
• Añadir, editar y eliminar participantes (equipos, oradores, jueces).
• Ver y registrar feedbacks para participantes o jueces.
• Asignar roles y permisos a otros administradores del torneo.

Módulo de Participantes (Tournament - Participant side):
• Ver su perfil dentro del torneo.
• Consultar resultados por ronda.
• Ver clasificación general de equipos y oradores.
• Acceder a la lista de mociones (temas de debate o prueba).
• Ver lista completa de participantes, divididos por rol: jueces y debatientes.

Tech Stack:
• Django Rest Framework
• Supabase
• WebSockets o Django Channels
• Sistema de roles y permisos (usuarios, organizadores, jueces)

Entregables:
1. Código fuente del proyecto con documentación clara.
2. Manual de usuario para participantes y administradores.
3. Demostración en vivo del sistema completamente funcional.
4. Informe técnico detallado con:
- Diagrama de la base de datos
- Arquitectura general del sistema
- Descripción de módulos y flujos clave
- Capturas de pantalla e instrucciones de despliegue