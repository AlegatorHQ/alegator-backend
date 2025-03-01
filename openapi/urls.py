from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view

TITLE = "Alegator-backend"
DESCRIPTION = """
Alegator is a SaaS platform designed to streamline the organization and management of debate tournaments. It provides a robust backend system for handling tournament structures, participant registrations, match scheduling, and automated tabulation. Built with scalability in mind, Alegator ensures seamless data management and real-time updates, making it an essential tool for debate organizers and institutions.
"""
VERSION = "1.0.0"


urlpatterns = [
    path(
        "schema/",
        get_schema_view(title=TITLE, description=DESCRIPTION, version=VERSION),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="openapi/swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
