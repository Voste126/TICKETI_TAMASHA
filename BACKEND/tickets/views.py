from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ticket
from events.models import Event
import qrcode
import os
from django.conf import settings
from django.http import JsonResponse

class TicketPurchaseView(APIView):
    def post(self, request, event_id):
        try:
            event = get_object_or_404(Event, id=event_id)
            if event.capacity <= 0:
                return Response({'error': 'Event is sold out'}, status=status.HTTP_400_BAD_REQUEST)

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

            return JsonResponse({
                'message': 'Ticket purchased successfully',
                'ticket_id': ticket.id,
                'qr_code_path': qr_code_path
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
