import uuid
from django.db import models


class StudentCourseStatus(models.TextChoices):
    ACCEPTED = "accepted"
    PENDING = "pending"


class StudentCourse(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    status = models.CharField(
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING,
    )
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
