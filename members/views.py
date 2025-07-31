from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from .models import CustomUser, Transaction, Payment
from .forms import CustomUserCreationForm, TransactionForm, PaymentForm, LoginForm

def login_view(request):
    """
    Handles user login.
    If the form is submitted with valid credentials, the user is logged in and redirected to the dashboard.
    """
    form = LoginForm()
    error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']
            
            user = authenticate(request, mobile_number=mobile_number, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error = "Invalid mobile number or password."
    
    return render(request, 'members/login.html', {'form': form, 'error': error})

def register_view(request):
    """
    Handles user registration.
    If the form is submitted and valid, a new user is created and redirected to the login page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'members/register.html', {'form': form})

@login_required
def dashboard_view(request):
    """
    Displays the user dashboard with a summary of financial data.
    - Total dues owed by the user
    - Total balance of the society
    - Recent transactions
    """
    user_payments = Payment.objects.filter(user=request.user)
    total_dues = user_payments.filter(is_paid=False).aggregate(Sum('amount_due'))['amount_due__sum'] or 0

    total_income = Transaction.objects.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    current_balance = total_income - total_expense

    recent_transactions = Transaction.objects.order_by('-date')[:5]

    context = {
        'user': request.user,
        'total_dues': total_dues,
        'current_balance': current_balance,
        'recent_transactions': recent_transactions,
        'app_name': 'HES Resident Hub',
    }
    return render(request, 'members/dashboard.html', context)

def logout_view(request):
    """Logs the user out and redirects to the login page."""
    logout(request)
    return redirect('login')

@login_required
def member_list_view(request):
    """Displays a list of all society members."""
    members = CustomUser.objects.all()
    context = {
        'members': members,
        'app_name': 'HES Resident Hub',
    }
    return render(request, 'members/member_list.html', context)

@login_required
def pay_dues_view(request):
    """Handles the form for paying dues."""
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment logic here
            return redirect('dashboard')
    
    return render(request, 'members/pay_dues.html', {'form': form, 'app_name': 'HES Resident Hub'})

@login_required
def add_transaction_view(request):
    """Handles the form for adding a new transaction."""
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    return render(request, 'members/add_transaction.html', {'form': form, 'app_name': 'HES Resident Hub'})

@login_required
def transaction_list_view(request):
    """
    Displays a list of all transactions.
    This is a placeholder for now and will display a simple message.
    """
    return render(request, 'members/coming_soon.html', {'app_name': 'HES Resident Hub', 'page_title': 'Transactions'})


def get_user_details_api(request, house_no):
    """
    Placeholder view for a user details API endpoint.
    This will prevent an AttributeError while you work on other parts of the app.
    """
    if request.method == 'GET':
        try:
            user = get_object_or_404(CustomUser, house_no=house_no)
            user_data = {
                'name': user.name,
                'mobile_number': user.mobile_number,
                'house_no': user.house_no
            }
            return JsonResponse(user_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=404)
    return HttpResponse(status=405) # Method Not Allowed
 