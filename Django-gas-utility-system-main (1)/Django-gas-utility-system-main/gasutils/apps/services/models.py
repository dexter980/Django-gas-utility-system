from django.db import models
from apps.accounts.models import CustomUser 

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak Report'),
        ('METER_ISSUE', 'Meter Issue'),
        ('BILLING', 'Billing Inquiry'),
        ('CONNECTION', 'New Connection'),
        ('OTHER', 'Other')
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.status}"