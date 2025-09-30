# from django.contrib import admin
# from django.urls import path
# from mic_general import views

# urlpatterns = [
#     path('',views.home, name='home'), 
#     path('schedule/',views.schedule, name='schedule'),
#     path('team/',views.team, name='team'),
#     path('about/',views.about, name='about'),
#     path('login/',views.login, name='login'),
#     path('team/<str:team_name>/', views.team_detail, name='team_detail'),
# ]

from django.urls import path
from mic_general import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('schedule/', views.schedule, name='schedule'),
    path('team/', views.team, name='team'),  # This should list all teams
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    # path('team/<str:team_name>/', views.team_detail, name='team_detail'),  # This shows a single team's detail
]