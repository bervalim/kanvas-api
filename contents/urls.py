from django.urls import path

from contents.views import CreateContentView, RetrieveUpdateDestroyContentView


urlpatterns = [
    path("courses/<course_id>/contents/", CreateContentView.as_view()),
    path(
        "courses/<course_id>/contents/<content_id>/",
        RetrieveUpdateDestroyContentView.as_view(),
    ),
]
