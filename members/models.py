# society_fund_app/members/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from datetime import date

# Custom User Manager for handling user creation with mobile number
class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError('The Mobile Number must be set')
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mobile_number, password, **extra_fields)

# Custom User Model to use mobile number for authentication
class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    mobile_number = models.CharField(unique=True, max_length=15)
    name = models.CharField(max_length=255)
    house_no = models.CharField(unique=True, max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['name', 'house_no']

    def __str__(self):
        return f"{self.name} ({self.house_no})"

# Model for monthly payments
class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    month = models.IntegerField()
    year = models.IntegerField(default=date.today().year)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.user.name} for month {self.month}/{self.year}"

# Model for all transactions (income and expense)
class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"

# --- New models for extended functionality ---

class Meeting(models.Model):
    """
    Model to store details of society meetings.
    """
    title = models.CharField(max_length=255)
    agenda = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_meetings')
    attendees = models.ManyToManyField(CustomUser, related_name='attended_meetings', blank=True)

    def __str__(self):
        return f"Meeting: {self.title} on {self.date}"

class ActionItem(models.Model):
    """
    Model to track actionable items from a meeting.
    """
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='action_items')
    task = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Task for {self.meeting.title}: {self.task}"

class Complaint(models.Model):
    """
    Model for members to raise suggestions or complaints.
    """
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    raised_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='complaints')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    date_raised = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint from {self.raised_by.name}: {self.title}"

class Event(models.Model):
    """
    Model for society events.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='organized_events')

    def __str__(self):
        return f"Event: {self.title} on {self.date}"
