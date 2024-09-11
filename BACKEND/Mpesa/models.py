# Create your models here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
import os


cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def home(request):
    return HttpResponse('Welcome to Django Daraja')

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = os.environ.get('MPESA_PHONE_NUMBER')
    amount = 1
    account_reference = 'Reference'
    transaction_desc = 'Test STK PUSH'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)



def stk_push_success(request):
	cl = MpesaClient()
	phone_number = os.environ.get('MPESA_PHONE_NUMBER')
	amount = 1
	account_reference = 'Django_STK_PUSH'
	transaction_desc = 'STK PUSH TEST'
	callback_url = stk_push_callback_url
	response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(response, safe=False)
	


def business_payment_success(request):
	phone_number = os.environ.get('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Business Payment Description'
	occassion = 'Test business payment occassion'
	callback_url = b2c_callback_url
	r = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)




def salary_payment_success(request):
	phone_number = os.environ.get('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Salary Payment Description'
	occassion = 'Test salary payment occassion'
	callback_url = b2c_callback_url
	r = cl.salary_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)



def promotion_payment_success(request):
	phone_number = os.environ.get('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Promotion Payment Description'
	occassion = 'Test promotion payment occassion'
	callback_url = b2c_callback_url
	r = cl.promotion_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)
