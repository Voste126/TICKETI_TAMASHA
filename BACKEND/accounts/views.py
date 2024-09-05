from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .tokens import create_jwt_token

from .serializers import SignUpSerializer
# Create your views here.

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    serializer_class = SignUpSerializer
    permission_classes = []

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

    def post(self, request: Request):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            token = create_jwt_token(user)

            return Response(
                data={"message": "Login Successful", "token": token},
                status=status.HTTP_200_OK
            )
        return Response(data={"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        return Response(data={"message": "Welcome to the Ticketi Tamasha API"}, status=status.HTTP_200_OK)

