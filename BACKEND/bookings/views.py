from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Bookings
from .serializer import BookingsSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

#Bookings Management APIView
class BookingsViewSet(viewsets.ViewSet):

    # get all bookings
    @swagger_auto_schema(operation_description="Get all bookings", responses={200: BookingsSerializer(many=True)}, operation_summary="Get all bookings")
    def list(self, request):
        queryset = Bookings.objects.all()
        serializer = BookingsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new booking
    @swagger_auto_schema(operation_description="Create a new booking", request_body=BookingsSerializer, responses={201: BookingsSerializer()}, operation_summary="Create a new booking")
    def create(self, request):
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get a specific booking
    @swagger_auto_schema(operation_description="Get a specific booking", responses={200: BookingsSerializer()}, operation_summary="Get a specific booking")
    def retrieve(self, request, pk=None):
        queryset = Bookings.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        serializer = BookingsSerializer(booking)
        return Response(serializer.data)
    
    # update a specific booking
    @swagger_auto_schema(operation_description="Update a specific booking", request_body=BookingsSerializer, responses={200: BookingsSerializer()}, operation_summary="Update a specific booking")
    def update(self, request, pk=None):
        booking = Bookings.objects.get(pk=pk)
        serializer = BookingsSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a specific booking
    @swagger_auto_schema(operation_description="Delete a specific booking", operation_summary="Delete a specific booking")
    def destroy(self, request, pk=None):
        booking = Bookings.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)