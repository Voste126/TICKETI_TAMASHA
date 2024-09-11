"""
URL configuration for Tamasha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import EventViewSet
from tickets.views import TicketViewSet
from accounts.views import SignUpView, LoginView
from bookings.views import BookingsViewSet
from payments.views import PaymentViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Ticketi Tamasha API",
        default_version='v1',
        description="All the APIs for the Ticketi Tamasha project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    #Events API for Ticketi tamasha
    path('api/events/', EventViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/events/<uuid:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    #Tickets API for Ticketi tamasha
    path('api/tickets/', TicketViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/tickets/<pk>/', TicketViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    #Accounts API for Ticketi tamasha
    path('auth/signup/', SignUpView.as_view()),
    path('auth/login/', LoginView.as_view()),

    #Bookings API for Ticketi tamasha
    path('api/bookings/', BookingsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/bookings/<pk>/', BookingsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    #Payments API for Ticketi tamasha
    path('api/payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/payments/<pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include('Mpesa.urls'))
]
