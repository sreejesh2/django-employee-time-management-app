from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer
from .models import CustomUser

# Create your views here.

class UserCreationView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()




from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=400)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name':user.first_name,
                    'last_name':user.last_name
                    # Add any additional user details you want to include
                }
            })

        return Response({'error': 'Invalid email or password'}, status=400)


