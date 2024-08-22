from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema  # for custom swagger documentation

#Ticket Management APIView
class TicketViewSet(viewsets.ViewSet):
    @swagger_auto_schema(operation_description="Get all tickets", responses={200: TicketSerializer(many=True)}, operation_summary="Get all tickets")
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new ticket", request_body=TicketSerializer, responses={201: TicketSerializer()}, operation_summary="Create a new ticket")
    def create(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_description="Get a specific ticket", responses={200: TicketSerializer()}, operation_summary="Get a specific ticket")
    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update a specific ticket", request_body=TicketSerializer, responses={200: TicketSerializer()}, operation_summary="Update a specific ticket")
    def update(self, request, pk=None):
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_description="Delete a specific ticket", operation_summary="Delete a specific ticket")
    def destroy(self, request, pk=None):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    