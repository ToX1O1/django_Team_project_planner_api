from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('create_team/', create_team),
    path('list_teams/',list_teams),
    path('describe_team/',describe_team),
    path('update_team/',update_team),
    path('add_user/',add_user),
    path('list_team_user/',list_team_user),
    path('delete_team_user/',delete_user)
]