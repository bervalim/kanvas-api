from rest_framework.permissions import SAFE_METHODS, BasePermission

from accounts.models import Account


class IsCourseStudentOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        if request.method in SAFE_METHODS and request.user in obj.course.students.all():
            return True
        return request.user.is_authenticated and request.user.is_superuser
