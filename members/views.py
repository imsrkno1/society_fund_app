# members/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm

# This is a hardcoded user for demonstration purposes.
# In a real application, you would check a database for user credentials.
DEMO_USER = {
    'mobile_number': '1234567890',
    'password': 'password123'
}

def login_view(request):
    """
    Handles form submission and renders the login page.
    - If the request is a GET, it shows an empty login form.
    - If the request is a POST, it validates the form data.
      - On successful login, it redirects to the 'index' page.
      - On failed login, it re-renders the form with an error message.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']

            # Check if the submitted credentials match the hardcoded user.
            if mobile_number == DEMO_USER['mobile_number'] and password == DEMO_USER['password']:
                # If credentials are correct, redirect to the 'index' URL.
                return redirect(reverse('index'))
            else:
                # If credentials are wrong, show the form again with an error.
                error = "Invalid mobile number or password."
                return render(request, 'members/login.html', {'form': form, 'error': error})
    else:
        # For a GET request, create a new, empty form.
        form = LoginForm()

    # Render the login template with the form.
    return render(request, 'members/login.html', {'form': form})

def index_view(request):
    """
    Renders the page that a user sees after a successful login.
    """
    return render(request, 'members/index.html')
