from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "name", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(username=validated_data['username'],
                                         name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserTokenSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("telegram_token",)