from rest_framework import serializers

from students_courses.models import StudentCourse


class StudentCourseSerialiazer(serializers.ModelSerializer):
    student_id = serializers.UUIDField(
        read_only=True,
        source="student.id",
    )
    student_username = serializers.CharField(
        max_length=150, source="student.username", read_only=True
    )
    student_email = serializers.CharField(
        max_length=150,
        source="student.email",
    )

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "status",
            "student_id",
            "student_username",
            "student_email",
        ]
