from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
# Create your views here.

class RegisterView(APIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


