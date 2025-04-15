from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

class RegisterAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "status": "success",
            "message": "User created successfully",
            "data": {
                "user_id": user.id,
                "email": user.email
            }
        }, status=status.HTTP_201_CREATED)

class UserProfileAPIView(generics.RetrieveAPIView):
    """
    API endpoint for user profile
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user