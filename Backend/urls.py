from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'users/?', UserApiView.as_view(), name="Users"),
    path('users/<int:pk>', UserDetail.as_view()),
    re_path(r'ideas/?', IdeaApiView.as_view(), name="Ideas"),
    path('ideas/<int:pk>', IdeaDetail.as_view())
]
