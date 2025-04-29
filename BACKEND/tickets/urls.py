from django.urls import path
from .views import TicketPurchaseView, StripePaymentSimulationView, MPESAPaymentSimulationView, EventTicketsView

urlpatterns = [
    path('events/<int:event_id>/purchase/', TicketPurchaseView.as_view(), name='ticket_purchase'),
]

urlpatterns += [
    path('events/<int:event_id>/stripe-payment/', StripePaymentSimulationView.as_view(), name='stripe_payment_simulation'),
    path('events/<int:event_id>/mpesa-payment/', MPESAPaymentSimulationView.as_view(), name='mpesa_payment_simulation'),
]

urlpatterns += [
    path('events/<int:event_id>/tickets/', EventTicketsView.as_view(), name='event_tickets'),
]