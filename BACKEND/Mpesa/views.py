from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_daraja.mpesa.core import MpesaClient
import os

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

@api_view(['GET'])
def home(request):
    """Welcome to Django Daraja API"""
    return Response({'message': 'Welcome to Django Daraja API'}, status=status.HTTP_200_OK)

class STKPushView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Test STK Push"""
        phone_number = os.environ.get('MPESA_PHONE_NUMBER')
        amount = request.data.get('amount', 1)  # Default to 1 if amount not provided
        account_reference = 'Reference'
        transaction_desc = 'Test STK Push'
        callback_url = stk_push_callback_url

        try:
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def oauth_success(request):
    """Get Access Token"""
    try:
        response = cl.access_token()
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

