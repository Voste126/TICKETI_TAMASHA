from django.urls import path
from .views import LoginView,  RegistrationView, LogoutView, PasswordResetRequestView, PasswordResetVerifyView, UpdateCredentialsView

urlpatterns = [
    path('update-credentials/', UpdateCredentialsView.as_view(), name='update_credentials'),
    path('password-reset/request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/verify/', PasswordResetVerifyView.as_view(), name='password_reset_verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
]