from django.urls import path, include
from rest_framework import routers
from .api import LoginAPI,RegisterAPI

router = routers.DefaultRouter()


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/login',LoginAPI.as_view()),
    path('api/auth/register/',RegisterAPI.as_view()),
]