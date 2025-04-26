from django.urls import path
from .views import TicketPurchaseView

urlpatterns = [
    path('events/<int:event_id>/purchase/', TicketPurchaseView.as_view(), name='ticket_purchase'),
]