from rest_framework import serializers
from contents.serializers import ContentSerializer
from courses.models import Course
from students_courses.serializers import StudentCourseSerialiazer
from .models import CourseStatus


class CourseSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED,
    )
    contents = ContentSerializer(read_only=True, many=True)
    students_courses = StudentCourseSerialiazer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    students_courses = StudentCourseSerialiazer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
