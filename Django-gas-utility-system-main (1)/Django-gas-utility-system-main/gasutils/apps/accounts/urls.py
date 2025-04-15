from django.urls import path
from .views import RegisterAPIView, UserProfileAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]