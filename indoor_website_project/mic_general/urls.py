from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('team/', views.team_view, name='team'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    
    # This is the dynamic path for a single team's detail page
    path('team/<str:team_name>/', views.team_detail_view, name='team_detail'),
]
