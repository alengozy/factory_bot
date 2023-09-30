import telegram
from django.conf import settings
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Messages

telegram_bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = ["id", "text", "date_posted"]

    def create(self, validated_data):
        user = validated_data['user']
        text = validated_data['text']

        if user.telegram_session_id:
            telegram_bot.send_message(chat_id=user.telegram_session_id,
                                      text=f"{user.name}, я получил от тебя сообщение:\n{text}")
        else:
            raise ValidationError(
                "Не удалось отправить сообщение, чат не привязан к пользователю.")

        return Messages.objects.create(text=text, user=user)
