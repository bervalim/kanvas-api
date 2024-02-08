from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from contents.models import Content
from contents.permissions import IsCourseStudentOrAdmin
from contents.serializers import ContentSerializer
from courses.models import Course
from courses.permissions import IsSuperUserAndAuthenticated


class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course_id = self.kwargs["course_id"]
        course_instance = Course.objects.get(id=course_id)
        serializer.save(course=course_instance)


class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        IsCourseStudentOrAdmin,
    ]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs["course_id"])
            content = Content.objects.get(pk=self.kwargs["content_id"])

        except Course.DoesNotExist:
            raise NotFound(
                {"detail": "course not found."},
            )

        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})

        self.check_object_permissions(self.request, content)

        return content
