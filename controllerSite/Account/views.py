from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# ... your other views may be here ...

def team_view(request):
    # For now, we are just showing the page. Later, you can pass team data from the database here.
    context = {}
    return render(request, 'teams.html', context)
