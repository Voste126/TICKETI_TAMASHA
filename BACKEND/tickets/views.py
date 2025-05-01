# This file contains API views for ticket-related operations, including purchasing tickets and simulating payments.
# It also includes QR code generation for purchased tickets.

from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Ticket
from events.models import Event
import qrcode
import os
from django.conf import settings
from .serializers import (
    TicketPurchasePayloadSerializer,
    TicketPurchaseResponseSerializer,
    StripePaymentPayloadSerializer,
    StripePaymentResponseSerializer,
    MPESAPaymentPayloadSerializer,
    MPESAPaymentResponseSerializer,
    TicketSerializer
)
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

class TicketPurchaseView(APIView):
    @swagger_auto_schema(
        operation_summary="Purchase Ticket",
        operation_description="Purchases a ticket for a specified event and generates a QR code.",
        request_body=TicketPurchasePayloadSerializer,
        responses={
            201: TicketPurchaseResponseSerializer,
            400: "Event is sold out.",
            500: "An error occurred during the purchase."
        }
    )
    def post(self, request, event_id):
        try:
            event = get_object_or_404(Event, id=event_id)
            if event.capacity <= 0:
                return Response({"message": "Event is sold out."}, status=400)

            price_paid = event.price_KES
            ticket = Ticket.objects.create(
                event=event,
                user=request.user,
                price_paid=price_paid
            )

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(ticket.id))
            qr.make(fit=True)
            qr_code_path = os.path.join(settings.MEDIA_ROOT, f'qr_codes/{ticket.id}.png')
            os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
            qr_code_image = qr.make_image(fill_color="black", back_color="white")
            qr_code_image.save(qr_code_path)

            return Response({
                "message": "Ticket purchased successfully.",
                "ticket_id": str(ticket.id),
                "qr_code_path": qr_code_path
            }, status=201)

        except Exception as e:
            return Response({"message": "An error occurred.", "error": str(e)}, status=500)

class StripePaymentSimulationView(APIView):
    @swagger_auto_schema(
        operation_summary="Simulate Stripe Payment",
        operation_description="Simulates a Stripe payment for a ticket associated with a specific event and generates a QR code.",
        request_body=StripePaymentPayloadSerializer,
        responses={
            200: StripePaymentResponseSerializer,
            404: "No ticket found for this event and user.",
            500: "An error occurred during the simulation."
        }
    )
    def post(self, request, event_id):
        try:
            event = get_object_or_404(Event, id=event_id)
            ticket = Ticket.objects.filter(event=event, user=request.user).first()
            if not ticket:
                return Response({"message": "No ticket found for this event and user."}, status=404)

            ticket.payment_method = 'stripe'
            ticket.payment_status = 'completed'
            ticket.save()

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(ticket.id))
            qr.make(fit=True)
            qr_code_path = os.path.join(settings.MEDIA_ROOT, f'qr_codes/{ticket.id}.png')
            os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
            qr_code_image = qr.make_image(fill_color="black", back_color="white")
            qr_code_image.save(qr_code_path)

            return Response({
                "message": "Stripe payment simulated successfully.",
                "ticket_id": str(ticket.id),
                "qr_code_path": qr_code_path
            }, status=200)
        except Exception as e:
            return Response({"message": "An error occurred.", "error": str(e)}, status=500)

class MPESAPaymentSimulationView(APIView):
    @swagger_auto_schema(
        operation_summary="Simulate MPESA Payment",
        operation_description="Simulates an MPESA payment for a ticket associated with a specific event and generates a QR code.",
        request_body=MPESAPaymentPayloadSerializer,
        responses={
            200: MPESAPaymentResponseSerializer,
            404: "No ticket found for this event and user.",
            500: "An error occurred during the simulation."
        }
    )
    def post(self, request, event_id):
        try:
            event = get_object_or_404(Event, id=event_id)
            ticket = Ticket.objects.filter(event=event, user=request.user).first()
            if not ticket:
                return Response({"message": "No ticket found for this event and user."}, status=404)

            ticket.payment_method = 'mpesa'
            ticket.payment_status = 'completed'
            ticket.save()

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(ticket.id))
            qr.make(fit=True)
            qr_code_path = os.path.join(settings.MEDIA_ROOT, f'qr_codes/{ticket.id}.png')
            os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
            qr_code_image = qr.make_image(fill_color="black", back_color="white")
            qr_code_image.save(qr_code_path)

            return Response({
                "message": "MPESA payment simulated successfully.",
                "ticket_id": str(ticket.id),
                "qr_code_path": qr_code_path
            }, status=200)
        except Exception as e:
            return Response({"message": "An error occurred.", "error": str(e)}, status=500)

class EventTicketsView(APIView):
    """
    API view to retrieve all tickets bought for a specific event.
    Accessible by event managers and admins.
    """
    @swagger_auto_schema(
        operation_summary="Get Tickets for an Event",
        operation_description="Retrieve all tickets purchased for a specific event.",
        responses={
            200: TicketSerializer(many=True),
            404: "Event not found."
        }
    )
    @permission_classes([IsAdminUser])
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        tickets = Ticket.objects.filter(event=event)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=200)
