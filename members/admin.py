from django.contrib import admin
from .models import CustomUser, Payment, Transaction, Meeting, ActionItem, Complaint, Event

# Register your models here to make them available in the Django admin interface.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'name', 'house_no', 'is_staff', 'is_active')
    search_fields = ('mobile_number', 'name', 'house_no')
    list_filter = ('is_staff', 'is_active')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_due', 'is_paid', 'month', 'year')
    list_filter = ('is_paid', 'month', 'year')
    search_fields = ('user__name', 'user__house_no')
    list_editable = ('is_paid',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'transaction_type', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ('title',)

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'created_by')
    list_filter = ('date',)
    search_fields = ('title', 'created_by__name')

class ActionItemAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'task', 'assigned_to', 'is_completed', 'due_date')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('task', 'assigned_to__name')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'raised_by', 'status', 'date_raised')
    list_filter = ('status',)
    search_fields = ('title', 'raised_by__name')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'location')


# Register the models with their respective admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(ActionItem, ActionItemAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Event, EventAdmin)

