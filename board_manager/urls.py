from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('create_board/',create_board),
    path('close_board/',close_board),
    path('add_task/',add_task),
    path('update_task/,',update_task),
    path('list_boards/',list_boards),
    path('export_board/',export_board)
]