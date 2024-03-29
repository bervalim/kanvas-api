from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import CreateAccountView


urlpatterns = [
    path("accounts/", CreateAccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
