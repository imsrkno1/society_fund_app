# members/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# The view for user registration.
def register_view(request):
    """
    Handles user registration.
    - On a GET request, it displays an empty registration form.
    - On a POST request, it attempts to validate and save the new user.
    """
    # If the user is already authenticated, redirect them to the index page.
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    # NOTE: The template path has been updated to 'members/register.html'
    return render(request, 'members/register.html', {'form': form})

# The view for user login.
def login_view(request):
    """
    Handles user login.
    - On a GET request, it displays an empty login form.
    - On a POST request, it attempts to authenticate the user.
    """
    # If the user is already authenticated, redirect them to the index page.
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('index')
    else:
        form = AuthenticationForm()
        
    # NOTE: The template path has been updated to 'members/login.html'
    return render(request, 'members/login.html', {'form': form})

# The view for logging out a user.
@login_required
def logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('login')

# The main index page, which is only accessible to authenticated users.
@login_required
def index_view(request):
    """
    The main page for authenticated users.
    The `@login_required` decorator ensures that only logged-in users can access this page.
    """
    # NOTE: The template path has been updated to 'members/index.html'
    return render(request, 'members/index.html')
