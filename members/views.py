from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm

# This is a hardcoded user for demonstration purposes.
# In a real application, you would check a database for user credentials.
DEMO_USER = {
    'mobile_number': '1234567890',
    'password': 'password123'
}

# The main view for the login page.
def login_view(request):
    # Check if the request method is POST. This happens when the form is submitted.
    if request.method == 'POST':
        # Create a form instance from the submitted data.
        form = LoginForm(request.POST)
        
        # Validate the form.
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']

            # Check if the submitted credentials match our hardcoded user.
            if mobile_number == DEMO_USER['mobile_number'] and password == DEMO_USER['password']:
                # If credentials are correct, redirect to the 'index' page.
                # You would normally handle a session here to keep the user logged in.
                return redirect(reverse('index'))
            else:
                # If credentials are wrong, render the same page with an error message.
                error = "Invalid mobile number or password."
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        # If the request method is GET (i.e., the user is just visiting the page),
        # create a new, empty form and render the login page.
        form = LoginForm()

    # Render the login.html template with the form.
    return render(request, 'login.html', {'form': form})

# A simple view for the page after a successful login.
def index_view(request):
    return render(request, 'index.html')
