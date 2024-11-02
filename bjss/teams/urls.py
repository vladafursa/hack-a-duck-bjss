from .views import teams_list_view, create_team
from django.urls import path

urlpatterns = [
    path('teams/', teams_list_view, name='teams-list'),
    path('create-team/', create_team, name='create_team'),
]