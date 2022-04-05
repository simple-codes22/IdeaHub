from django.urls import path, re_path
from .views import index

# Base URL router for the Frontend react application
app_name = 'Frontend'

urlpatterns = [
    re_path(r'.*', index),
]