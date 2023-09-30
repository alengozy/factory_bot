from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Messages
from .serializers import MessagesSerializer

# Create your views here.
class MessagesViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Messages.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)