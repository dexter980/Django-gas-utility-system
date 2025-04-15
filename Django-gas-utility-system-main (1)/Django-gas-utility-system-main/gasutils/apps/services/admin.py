from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_email', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('user__email', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'User Email'