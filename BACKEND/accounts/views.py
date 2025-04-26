from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.serializers import Serializer, CharField, EmailField, ValidationError
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random

class LoginView(TokenObtainPairView):
    """
    Handles user login and returns JWT tokens.
    """
    pass

class RegistrationView(APIView):
    """
    Handles user registration.
    """
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        otp = random.randint(100000, 999999)
        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is {otp}',
            'noreply@tiketitamasha.com',
            [email],
        )

        request.session['password_reset_otp'] = otp
        request.session['password_reset_email'] = email

        return Response({'message': 'Password reset OTP sent successfully'}, status=status.HTTP_200_OK)

class PasswordResetVerifyView(APIView):
    def post(self, request):
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')
        email = request.session.get('password_reset_email')
        session_otp = request.session.get('password_reset_otp')

        if not otp or not new_password or not email or not session_otp:
            return Response({'error': 'Invalid OTP or session expired'}, status=status.HTTP_400_BAD_REQUEST)

        if int(otp) != session_otp:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)

class UpdateCredentialsView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        data = request.data

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.gender = data.get('gender', user.gender)

        if 'password' in data:
            user.set_password(data['password'])

        user.save()
        return Response({"message": "User credentials updated successfully."}, status=status.HTTP_200_OK)
