from django.urls import path
from .views import verify_faces

urlpatterns = [
    path('verify/', verify_faces, name='verify_faces'),
]