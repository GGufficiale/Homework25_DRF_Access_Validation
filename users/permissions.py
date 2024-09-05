from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    message = 'You are not a moderator'

    def has_permission(self, request, view):
        """Метод ограничения доступа для всех кроме модераторов из админки"""
        return request.user.groups.filter(name='moderator').exists()

