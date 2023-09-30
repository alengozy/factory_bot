from rest_framework import serializers
from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["id", "text", "date_posted"]

    def create(self, validated_data):
        message = Messages.objects.create(text=validated_data['text'],
                                          user=validated_data['user'])

        return message