from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Event
from .serializer import EventSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.permissions import IsAuthenticated

#Event Management APIView
class EventViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    # get all events
    @swagger_auto_schema(operation_description="Get all events", responses={200: EventSerializer(many=True)}, operation_summary="Get all events")
    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new event
    @swagger_auto_schema(operation_description="Create a new event", request_body=EventSerializer, responses={201: EventSerializer()}, operation_summary="Create a new event")
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get a specific event
    @swagger_auto_schema(operation_description="Get a specific event", responses={200: EventSerializer()}, operation_summary="Get a specific event")
    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    # update a specific event
    @swagger_auto_schema(operation_description="Update a specific event", request_body=EventSerializer, responses={200: EventSerializer()}, operation_summary="Update a specific event")
    def update(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a specific event
    @swagger_auto_schema(operation_description="Delete a specific event", operation_summary="Delete a specific event")
    def destroy(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    