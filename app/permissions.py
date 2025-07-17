from rest_framework import permissions

from .models import Usertournament


class TournamentsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
                and Usertournament.objects.filter(
                    tournament=obj, user=request.user, role="admin"
                ).exists()
            )

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "create":
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
