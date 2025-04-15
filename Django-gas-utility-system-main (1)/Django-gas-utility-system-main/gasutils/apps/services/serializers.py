from rest_framework import serializers
from .models import ServiceRequest
from apps.accounts.serializers import UserSerializer  

class ServiceRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    
    class Meta:
        model = ServiceRequest
        fields = ['id', 'user', 'request_type', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

class CreateServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description']