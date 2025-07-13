from rest_framework import permissions


class CheckinsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class DrawsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class FeedbacksPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # any authenticated user can update
            return request.user.is_authenticated

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class JudgesPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class RoundsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class SpeakerresultsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class SpeakersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class TeamresultsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class TeamsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the admins can update
            return request.user.is_authenticated and request.user.is_superuser

        if view.action == "destroy":
            # only the admins can delete
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True
