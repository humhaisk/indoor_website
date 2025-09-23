from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def schedule(request):
    return render(request, 'bracket.html')
def team(request):
    return render(request, 'team.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')