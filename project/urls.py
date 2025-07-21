from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app.urls import app_router
from sgtd.urls import sgtd_router

router = routers.DefaultRouter()
router.registry.extend(app_router.registry)
router.registry.extend(sgtd_router.registry)

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
]
