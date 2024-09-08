from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from .models import Ticket
from .serializer import TicketSerializer
from events.models import Event  # Import Event model

class TicketViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all tickets",
        responses={200: TicketSerializer(many=True)},
        operation_summary="Get all tickets"
    )
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new ticket",
        request_body=TicketSerializer,
        responses={201: TicketSerializer()},
        operation_summary="Create a new ticket"
    )
    def create(self, request):
        # Get the event ID from the request data
        event_id = request.data.get('event')
        # Validate that the event ID exists
        event = get_object_or_404(Event, event_id=event_id)

        # Create the ticket with the associated event
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event)  # Associate the ticket with the event
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Get a specific ticket",
        responses={200: TicketSerializer()},
        operation_summary="Get a specific ticket"
    )
    def retrieve(self, request, pk=None):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update a specific ticket",
        request_body=TicketSerializer,
        responses={200: TicketSerializer()},
        operation_summary="Update a specific ticket"
    )
    def update(self, request, pk=None):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific ticket",
        operation_summary="Delete a specific ticket"
    )
    def destroy(self, request, pk=None):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
