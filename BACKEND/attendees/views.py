from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AttendeeSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .tokens import create_jwt_pair_for_user

#Attendee Management APIView
class SignUpView(generics.GenericAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = []
    @swagger_auto_schema(operation_description="Sign Up", request_body=AttendeeSerializer, responses={201: AttendeeSerializer()}, operation_summary="Sign Up")
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    @swagger_auto_schema(operation_description="Login", responses={200: AttendeeSerializer()}, operation_summary="Login")
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Get User", responses={200: AttendeeSerializer()}, operation_summary="Get User")
    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)