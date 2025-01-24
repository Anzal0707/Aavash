from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class AppointmentRequest(models.Model):
    DEPARTMENTS = [
        ('Diagnostic', 'Diagnostic'),
        ('Psychological', 'Psychological'),
        ('Orthopedics', 'Orthopedics'), 
        ('General', 'General')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    department = models.CharField(max_length=50, choices=DEPARTMENTS)
    payment_proof = models.ImageField(upload_to='payment_proofs/', null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)  
    scheduled_time = models.TimeField(blank=True, null=True)  

    def __str__(self):
        return f"{self.name} - {self.date} - {'Confirmed' if self.confirmed else 'Pending'}"



class FollowUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Follow-up for {self.user.username} on {self.date}"
    
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report uploaded on {self.uploaded_at}"
    
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

