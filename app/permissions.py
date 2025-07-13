from rest_framework import permissions


class TournamentsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can read
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            # only the owner of the object can update
            return obj.creator == request.user

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


class UsertournamentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # nobody can read
            return False

        if view.action in ["update", "partial_update"]:
            # nobody can update
            return False

        if view.action == "destroy":
            # nobody can delete
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # nobody can list objects
            return False

        if view.action == "create":
            # nobody can create
            return False

        return True
