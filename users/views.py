from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserProfileForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.user_type == 'patient':
        return render(request, 'users/patient_dashboard.html', {'user': request.user})
    elif request.user.user_type == 'doctor':
        return render(request, 'users/doctor_dashboard.html', {'user': request.user})
    else:
        return redirect('login')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

def logout(request):
    django_logout(request)
    return redirect('login')