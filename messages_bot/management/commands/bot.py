from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from authentication.models import CustomUser


class Command(BaseCommand):
    help = """Telegram bot command to handle user messages and tokens.
    Usage: /start to initiate a conversation.
           /reset to reset your token.
    """

    def handle(self, *args, **kwargs):
        TOKEN_RESET = 'Token Reset! Please enter new token.'
        TOKEN_FOUND = 'Token found!'
        USER_NOT_FOUND = 'User not found!'
        OBSOLETE_TOKEN = 'Token is no longer valid. Please renew your token.'
        TOKEN_ADDED = 'Token has been successfully added!'

        def start(update, context):
            user_id = update.effective_user.id
            try:
                user = CustomUser.objects.get(telegram_session_id=user_id)
                update.message.reply_text(TOKEN_FOUND)
            except CustomUser.DoesNotExist:
                update.message.reply_text(USER_NOT_FOUND)

        def reset(update, context):
            user_id = update.effective_user.id
            try:
                user = CustomUser.objects.get(telegram_session_id=user_id)
                user.telegram_session_id = None
                user.save()
                update.message.reply_text(TOKEN_RESET)
            except CustomUser.DoesNotExist:
                update.message.reply_text(USER_NOT_FOUND)

        def handle_message(update, context):
            user_id = update.effective_user.id
            try:
                user = CustomUser.objects.get(telegram_session_id=user_id)
                update.message.reply_text(TOKEN_FOUND)
            except CustomUser.DoesNotExist:
                token = update.message.text.strip()
                try:
                    user = CustomUser.objects.get(telegram_token=token)
                except CustomUser.DoesNotExist:
                    update.message.reply_text(OBSOLETE_TOKEN)

                if user.telegram_session_id:
                    update.message.reply_text(OBSOLETE_TOKEN)
                else:
                    user.telegram_session_id = user_id
                    user.save()
                    update.message.reply_text(TOKEN_ADDED)

        updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(CommandHandler("reset", reset))
        updater.dispatcher.add_handler(
            MessageHandler(Filters.text & ~Filters.command, handle_message)
        )
        updater.start_polling()
        updater.idle()
