from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import CreateModelMixin
from .serializers import UserSerializer

from .models import CustomUser
# Create your views here.

class RegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    


