from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('list_user', list_users),
    path('create_user/', create_user),
    path('describe_user/',describe_user_view),
    path('update_user/',update_user_view),
    path('user_teams_view/',get_user_teams_view)
]