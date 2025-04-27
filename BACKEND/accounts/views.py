import random
import logging
from datetime import timedelta
from django.core.mail import send_mail
from django.utils.timezone import now
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .models import User
from .serializers import RegistrationSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


logger = logging.getLogger(__name__)


def generate_otp(user):
    otp = random.randint(100000, 999999)
    user.otp = otp
    user.otp_created_at = now()
    user.save()
    return otp


# Adding Swagger documentation to RegistrationAPIView
class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="User Registration",
        operation_description="Allows a new user to register by providing their details, including a strong password and role selection.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character.'
                ),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='User first name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='User last name'),
                'gender': openapi.Schema(type=openapi.TYPE_STRING, description='User gender'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='User phone number'),
                'role': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=['USER', 'EVENT_MANAGER', 'ADMIN'],
                    description='Role of the user. Choices are USER, EVENT_MANAGER, or ADMIN.'
                ),
            },
            required=['email', 'password', 'phone_number', 'role']
        ),
        responses={
            201: openapi.Response(description="User registered successfully."),
            400: openapi.Response(description="Invalid input data."),
            500: openapi.Response(description="An error occurred while processing your request."),
        }
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = generate_otp(user)
            try:
                send_mail(
                    subject="Verify Your Email",
                    message=f"Your OTP for email verification is: {otp}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                return Response(
                    {
                        "message": "User registered successfully. Check your email for the OTP to verify your account."
                    },
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response(
                    {"error": f"An error occurred while processing your request. {e}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Adding Swagger documentation to LoginAPIView
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Allows a user to log in by providing their email and password.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            },
            required=['email', 'password']
        ),
        responses={
            200: openapi.Response(description="Login successful."),
            400: openapi.Response(description="Invalid credentials."),
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


# Adding Swagger documentation to VerifyEmailAPIView
class VerifyEmailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Verify Email",
        operation_description="Allows a user to verify their email using an OTP.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
                'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP sent to the user email'),
            },
            required=['email', 'otp']
        ),
        responses={
            200: openapi.Response(description="Email verified successfully."),
            400: openapi.Response(description="Invalid or expired OTP."),
            404: openapi.Response(description="User not found."),
        }
    )
    def post(self, request):
        otp = request.data.get("otp")
        email = request.data.get("email")

        if not otp or not email:
            return Response(
                {"error": "OTP and email are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if user.otp != otp or user.otp_created_at < now() - timedelta(minutes=10):
            return Response(
                {"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST
            )

        user.email_verified = True
        user.otp = None
        user.otp_created_at = None
        user.save()

        return Response(
            {"message": "Email verified successfully."}, status=status.HTTP_200_OK
        )


# Adding Swagger documentation to LogoutAPIView
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="User Logout",
        operation_description="Allows an authenticated user to log out by providing their refresh token.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token of the user'),
            },
            required=['refresh_token']
        ),
        responses={
            200: openapi.Response(description="Logout successful."),
            400: openapi.Response(description="Invalid or expired token."),
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                logger.error("No refresh token provided in the request.")
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            logger.info(f"Received refresh token: {refresh_token}")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Ensure token is blacklisted

            logger.info("Token successfully blacklisted.")
            return Response(
                {"message": "Logout successful."}, status=status.HTTP_200_OK
            )
        except AttributeError as e:
            logger.error(f"AttributeError: {e}")
            return Response(
                {"error": "Token blacklisting is not enabled. Ensure the Blacklist app is configured."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except TokenError as e:
            logger.error(f"TokenError: {e}")
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )


# Adding Swagger documentation to ForgetPasswordAPIView
class ForgetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Request Password Reset OTP",
        operation_description="Allows a user to request an OTP for password reset by providing their email address.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
            },
            required=['email']
        ),
        responses={
            200: openapi.Response(description="OTP sent to your email."),
            400: openapi.Response(description="Email is required."),
            404: openapi.Response(description="User with this email does not exist."),
        }
    )
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            otp = generate_otp(user)
            send_mail(
                subject="Password Reset OTP",
                message=f"Your OTP for password reset is: {otp}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return Response({"message": "OTP sent to your email."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)


# Adding Swagger documentation to ResetPasswordAPIView
class ResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Reset Password",
        operation_description="Allows a user to reset their password using an OTP, email, and new password.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
                'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP sent to the user email'),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING, description='New password for the user'),
            },
            required=['email', 'otp', 'new_password']
        ),
        responses={
            200: openapi.Response(description="Password reset successfully."),
            400: openapi.Response(description="Invalid or expired OTP."),
            404: openapi.Response(description="User not found."),
        }
    )
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        new_password = request.data.get("new_password")

        if not email or not otp or not new_password:
            return Response({"error": "Email, OTP, and new password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.otp != otp or user.otp_created_at < now() - timedelta(minutes=10):
            return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.otp = None
        user.otp_created_at = None
        user.save()

        return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)


# Adding Swagger documentation to GenerateNewOTPView
class GenerateNewOTPView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Generate New OTP",
        operation_description="Allows an authenticated user to generate a new OTP.",
        responses={
            200: openapi.Response(description="New OTP sent to your email."),
        }
    )
    def post(self, request):
        user = request.user
        otp = generate_otp(user)
        send_mail(
            subject="New OTP Generated",
            message=f"Your new OTP is: {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return Response({"message": "New OTP sent to your email."}, status=status.HTTP_200_OK)
