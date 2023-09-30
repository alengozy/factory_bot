from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, DestroyModelMixin
from .models import Messages
from .serializers import MessagesSerializer

# Create your views here.
class MessagesViewSet(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet, DestroyModelMixin):
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Messages.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)