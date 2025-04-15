from django.urls import path
from .views import ServiceRequestListCreateView, ServiceRequestDetailView

app_name = 'services'

urlpatterns = [
    path('requests/', ServiceRequestListCreateView.as_view(), name='request-list'),
    path('requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='request-detail'),
]