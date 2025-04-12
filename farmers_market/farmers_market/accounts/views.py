from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:dashboard')  # Should redirect on success
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

@login_required
def dashboard_view(request):
    if request.user.role == 'farmer':
        return render(request, 'accounts/farmer_dashboard.html')
    elif request.user.role == 'buyer':
        return render(request, 'accounts/buyer_dashboard.html')
    return render(request, 'accounts/dashboard.html')  # fallback

def logout_view(request):
    logout(request)
    return redirect('accounts:login')
