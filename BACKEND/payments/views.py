from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from payments.models import Payment
from .serializer import PaymentSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
#Payment Management APIView
class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    # get all payments
    @swagger_auto_schema(operation_description="Get all payments", responses={200: PaymentSerializer(many=True)}, operation_summary="Get all payments")
    def list(self, request):
        queryset = Payment.objects.all()
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a payment
    @swagger_auto_schema(request_body=PaymentSerializer)
    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get a specific payment
    @swagger_auto_schema(operation_description="Get a specific payment", responses={200: PaymentSerializer()}, operation_summary="Get a specific payment")
    def retrieve(self, request, pk=None):
        queryset = Payment.objects.all()
        payment = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    
    # update a specific payment
    @swagger_auto_schema(operation_description="Update a specific payment", request_body=PaymentSerializer, responses={200: PaymentSerializer()}, operation_summary="Update a specific payment")
    def update(self, request, pk=None):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a specific payment
    @swagger_auto_schema(operation_description="Delete a specific payment", operation_summary="Delete a specific payment")
    def destroy(self, request, pk=None):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)