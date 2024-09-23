from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('create_profile')  # Redirect to create profile
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # Use Django's built-in authentication form
        if form.is_valid():
            email = form.cleaned_data.get('username')  # 'username' holds email in AuthenticationForm
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # Authenticate user by email
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid email or password.")  # Show error on invalid credentials
        else:
            messages.error(request, "Invalid email or password.")  # If the form itself is invalid
    else:
        form = AuthenticationForm()  # Empty form for GET request

    return render(request, 'account/login.html', {'form': form})  # Render login form

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
        return render(request, 'account/profile.html', {'profile': profile})
    except Profile.DoesNotExist:
        return redirect('create_profile')  # Redirect if profile does not exist

@login_required
def update_profile(request):
    profile = request.user.profile  # Get the user's profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to profile view after update
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'account/update_profile.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_view')  # Assuming this is the profile view URL
    else:
        form = ProfileForm()
    return render(request, 'account/create_profile.html', {'form': form})
