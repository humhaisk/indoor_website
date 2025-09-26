from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Match

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Edit Profile
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# Live Matches
def live_matches_view(request):
    live_matches = Match.objects.filter(is_live=True).order_by('game')
    return render(request, 'live_matches.html', {'live_matches': live_matches})

# My Matches
@login_required
def my_matches_view(request):
    my_matches = Match.objects.filter(player1=request.user) | Match.objects.filter(player2=request.user)
    return render(request, 'my_matches.html', {'my_matches': my_matches.order_by('is_completed')})
