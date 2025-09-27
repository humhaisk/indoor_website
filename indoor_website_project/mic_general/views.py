from django.shortcuts import render
from .models import Organizing_Committee

# View for the homepage
def home_view(request):
    return render(request, 'index.html')

# View for the schedule page
def schedule_view(request):
    return render(request, 'bracket.html')

# View for the page that lists all teams
def team_view(request):
    return render(request, 'team.html')

# View for a single team's detail page
def team_detail_view(request, team_name):
    context = {
        'team_name': team_name,
        'players': ['Player 1', 'Player 2', 'Player 3', 'Player 4'] # Placeholder data
    }
    return render(request, 'team_detail.html', context)

# View for the about page, which loads data from the database
def about_view(request):
    member_data = Organizing_Committee.objects.all()
    context = {'members': member_data}
    return render(request, 'about.html', context)

# View for the login page
def login_view(request):
    return render(request, 'login.html')