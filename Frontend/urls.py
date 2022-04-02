from django.urls import path
from .views import index

# Base URL router for the Frontend react application
app_name = 'Frontend'

urlpatterns = [
    path('', index, name='Index'),
]