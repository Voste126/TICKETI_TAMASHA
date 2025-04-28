from rest_framework import viewsets
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
            raise PermissionDenied("You do not have permission to create events.")
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        if request.user.role not in ['ADMIN', 'EVENT_MANAGER']:
            raise PermissionDenied("You do not have permission to update events.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role not in ['ADMIN', 'EVENT_MANAGER']:
            raise PermissionDenied("You do not have permission to delete events.")
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        # Short-circuit for schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Event.objects.none()

        if self.request.user.role == 'ADMIN':
            return Event.objects.all()
        return Event.objects.filter(created_by=self.request.user)
