from rest_framework import generics, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer, CreateServiceRequestSerializer

class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateServiceRequestSerializer
        return ServiceRequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]