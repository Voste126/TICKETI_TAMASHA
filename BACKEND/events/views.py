# This file contains a ModelViewSet for CRUD operations on events.
# It includes permission checks to restrict access based on user roles.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role not in ['ADMIN', 'EVENT_MANAGER']:
            return Response({"message": "You do not have permission to create events."}, status=403)
        serializer.save(created_by=self.request.user)
        return Response({"message": "Event created successfully."}, status=201)

    def update(self, request, *args, **kwargs):
        if request.user.role not in ['ADMIN', 'EVENT_MANAGER']:
            return Response({"message": "You do not have permission to update events."}, status=403)
        response = super().update(request, *args, **kwargs)
        return Response({"message": "Event updated successfully."}, status=200)

    def destroy(self, request, *args, **kwargs):
        if request.user.role not in ['ADMIN', 'EVENT_MANAGER']:
            return Response({"message": "You do not have permission to delete events."}, status=403)
        response = super().destroy(request, *args, **kwargs)
        return Response({"message": "Event deleted successfully."}, status=200)

    def get_queryset(self):
        # Short-circuit for schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Event.objects.none()

        if self.request.user.role == 'ADMIN':
            return Event.objects.all()
        return Event.objects.filter(created_by=self.request.user)
