from django.contrib import admin
from .models import AppointmentRequest
from django.utils.html import format_html
from .models import FollowUp
from .models import Report
from .models import ContactMessage


# Register your models here.

@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'department', 'confirmed', 'scheduled_time')
    list_filter = ('department', 'confirmed')
    search_fields = ('name', 'email', 'phone')

    def confirm_appointment(self, request, queryset):
        for appointment in queryset:
            appointment.confirmed = True
            # Set a default time if required (can also be set manually in admin)
            if not appointment.confirmed_time:
                appointment.confirmed_time = '10:00:00'  # Example: default confirmation time
            appointment.save()
        self.message_user(request, f"{queryset.count()} appointment(s) confirmed.")
    confirm_appointment.short_description = "Confirm selected appointments"

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('user', 'details', 'date')
    search_fields = ('user__username', 'details')

admin.site.register(FollowUp, FollowUpAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at')  # Display the user and other fields
    search_fields = ['user__username', 'uploaded_at']

    def payment_proof_preview(self, obj):
        if obj.payment_proof:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.payment_proof.url)
        return "No Image"
    payment_proof_preview.short_description = "Payment Proof"

admin.site.register(Report, ReportAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')
    ordering = ('-submitted_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)

