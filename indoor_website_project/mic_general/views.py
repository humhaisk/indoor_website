from django.shortcuts import render
from mic_general.models import Organizing_Committee

# Create your views here.
def home(request):
    return render(request, 'index.html')
def schedule(request):
    return render(request, 'bracket.html')
def team(request):
    return render(request, 'team.html')
def about(request):
    member_data = Organizing_Committee.objects.all()
    context = {'members': member_data}
    return render(request, 'about.html', context)
def login(request):
    return render(request, 'login.html')