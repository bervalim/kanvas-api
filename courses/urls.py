from django.urls import path
from courses.views import (
    AddStudentToCourseView,
    ListCreateCourseView,
    RetrieveUpdateDestroyCourseView,
)


urlpatterns = [
    path("courses/", ListCreateCourseView.as_view()),
    path("courses/<course_id>/", RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<course_id>/students/", AddStudentToCourseView.as_view()),
]
