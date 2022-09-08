from django.urls import path
from app_familiares.views import ver_familiares


urlpatterns = [
    path('', ver_familiares),
]