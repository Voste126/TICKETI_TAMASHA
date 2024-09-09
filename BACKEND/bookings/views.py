from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Bookings, Event, Ticket
from .serializer import BookingsSerializer

# Bookings Management APIView
class BookingsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    # Get all bookings
    @swagger_auto_schema(operation_description="Get all bookings", responses={200: BookingsSerializer(many=True)}, operation_summary="Get all bookings")
    def list(self, request):
        queryset = Bookings.objects.all()
        serializer = BookingsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new booking
    @swagger_auto_schema(operation_description="Create a new booking", request_body=BookingsSerializer, responses={201: BookingsSerializer()}, operation_summary="Create a new booking")
    def create(self, request):
        user = request.user  # Get the logged-in user from the request
        event_id = request.data.get('event')  # Extract event_id from request data
        ticket_id = request.data.get('ticket')  # Extract ticket_id from request data
        quantity = request.data.get('quantity')  # Extract quantity from request data

        # Validate event and ticket
        event = get_object_or_404(Event, event_id=event_id)
        ticket = get_object_or_404(Ticket, ticket_id=ticket_id)

        # Prepare the booking data
        booking_data = {
            'user': user.id,  # This is fine since the User model uses `id`
            'event': event.event_id,  # Use event.event_id instead of event.id
            'ticket': ticket.ticket_id,  # Use ticket.ticket_id instead of ticket.id
            'quantity': quantity
        }


        serializer = BookingsSerializer(data=booking_data)

        if serializer.is_valid():
            serializer.save(user=user)  # Save the booking with the user context
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get a specific booking
    @swagger_auto_schema(operation_description="Get a specific booking", responses={200: BookingsSerializer()}, operation_summary="Get a specific booking")
    def retrieve(self, request, pk=None):
        booking = get_object_or_404(Bookings, pk=pk)
        serializer = BookingsSerializer(booking)
        return Response(serializer.data)

    # Update a specific booking
    @swagger_auto_schema(operation_description="Update a specific booking", request_body=BookingsSerializer, responses={200: BookingsSerializer()}, operation_summary="Update a specific booking")
    def update(self, request, pk=None):
        booking = get_object_or_404(Bookings, pk=pk)
        serializer = BookingsSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific booking
    @swagger_auto_schema(operation_description="Delete a specific booking", operation_summary="Delete a specific booking")
    def destroy(self, request, pk=None):
        booking = get_object_or_404(Bookings, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)