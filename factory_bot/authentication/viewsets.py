import secrets
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, UserTokenSerializer

from .models import CustomUser
# Create your views here.

class RegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    

class UserTokenViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserTokenSerializer

    @action(methods=["PUT"], detail=False)
    def get_bot_token(self, request):
        user = CustomUser.objects.get(id=request.user.id)

        if not user.telegram_token:
            user.telegram_token = secrets.token_urlsafe(32)
            user.save()

        serializer = UserTokenSerializer(user)
        return Response(serializer.data)