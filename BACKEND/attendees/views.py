from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Attendee
from .serializer import AttendeeSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

#Attendee Management APIView
class AttendeeViewSet(viewsets.ViewSet):

    # get all attendees
    @swagger_auto_schema(operation_description="Get all attendees", responses={200: AttendeeSerializer(many=True)}, operation_summary="Get all attendees")
    def list(self, request):
        queryset = Attendee.objects.all()
        serializer = AttendeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new attendee
    @swagger_auto_schema(operation_description="Create a new attendee", request_body=AttendeeSerializer, responses={201: AttendeeSerializer()}, operation_summary="Create a new attendee")
    def create(self, request):
        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get a specific attendee
    @swagger_auto_schema(operation_description="Get a specific attendee", responses={200: AttendeeSerializer()}, operation_summary="Get a specific attendee")
    def retrieve(self, request, pk=None):
        queryset = Attendee.objects.all()
        attendee = get_object_or_404(queryset, pk=pk)
        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data)
    
    # update a specific attendee
    @swagger_auto_schema(operation_description="Update a specific attendee", request_body=AttendeeSerializer, responses={200: AttendeeSerializer()}, operation_summary="Update a specific attendee")
    def update(self, request, pk=None):
        attendee = Attendee.objects.get(pk=pk)
        serializer = AttendeeSerializer(attendee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a specific attendee
    @swagger_auto_schema(operation_description="Delete a specific attendee", operation_summary="Delete a specific attendee")
    def destroy(self, request, pk=None):
        attendee = Attendee.objects.get(pk=pk)
        attendee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)