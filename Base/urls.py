from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('Backend.urls')),
    path('admin/', admin.site.urls),
    path('', include('Frontend.urls')),
]
