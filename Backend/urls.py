from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserApiView.as_view(), name="Users"),
    path('users/<int:pk>', UserDetail.as_view()),
    path('ideas/', IdeaApiView.as_view(), name="Ideas"),
    path('ideas/<int:pk>', IdeaDetail.as_view())
]
