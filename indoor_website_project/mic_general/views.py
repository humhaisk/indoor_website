from django.shortcuts import render
from mic_general.models import Organizing_Committee
from mic_general.models import Team

# Create your views here.
def home(request):
    return render(request, 'index.html')
def schedule(request):
    return render(request, 'bracket.html')
# def team_detail(request, team_name):
#     team = 
#     return render(request, 'team_detail.html', {'team': team})
def team(request):
    teams_data = Team.objects.all()
    teams = {'teams': teams_data}
    return render(request, 'team.html', teams)
    # return render(request, 'team.html')
def about(request):
    member_data = Organizing_Committee.objects.all()
    context = {'members': member_data}
    return render(request, 'about.html', context)
def login(request):
    return render(request, 'login.html')