# This file maps URLs to views for user-related operations such as registration, login, and password management.

from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, VerifyEmailAPIView, LogoutAPIView, ForgetPasswordAPIView, ResetPasswordAPIView, GenerateNewOTPView


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify_email'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget_password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset_password'),
    path('generate-new-otp/', GenerateNewOTPView.as_view(), name='generate_new_otp'),
]