from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Account
from courses.models import Course
from courses.permissions import IsSuperUser, IsSuperUserAndAuthenticated
from courses.serializers import CourseSerializer, StudentSerializer
from students_courses.models import StudentCourse


class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user)


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"


class AddStudentToCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]
    queryset = Course.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = "course_id"

    def perform_update(self, serializer):
        students_courses = serializer.validated_data.get(
            "students_courses",
            [],
        )

        course_id = self.kwargs.get("course_id")
        try:
            course = get_object_or_404(Course, id=course_id)
        except Http404:
            error_message = {"detail": "course not found."}
            raise JsonResponse(error_message, status=status.HTTP_404_NOT_FOUND)

        emails_not_found = []
        for course_data in students_courses:
            email = course_data.get("student", {}).get("email")
            if email:
                try:
                    student = Account.objects.get(email=email)
                    StudentCourse.objects.create(
                        course=course,
                        student=student,
                    )
                    course.students.add(student)
                except Account.DoesNotExist:
                    emails_not_found.append(email)

        if emails_not_found:
            email_list = ", ".join(emails_not_found)
            raise ValidationError(
                {"detail": f"No active accounts was found: {email_list}."}
            )
