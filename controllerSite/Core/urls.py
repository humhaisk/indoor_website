from django.contrib import admin
from django.urls import path, include
from Core import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('matches/live/', views.live_matches_view, name='live_matches'),
    path('matches/my/', views.my_matches_view, name='my_matches'),
]