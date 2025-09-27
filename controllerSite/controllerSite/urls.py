from django.urls import path
from . import views

urlpatterns = [
    # Assuming you have a homepage view
    # path('', views.home_view, name='home'),

    # Assuming you have a schedule page view
    # path('schedule/', views.schedule_view, name='schedule'),

    # Path for the list of all teams
    path('team/', views.team_view, name='team'),

    # Dynamic path for a single team's details
    path('team/<str:team_name>/', views.team_detail_view, name='team_detail'),
]