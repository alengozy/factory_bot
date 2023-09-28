from django.core.management.base import BaseCommand
from django.conf import settings



class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Test Command'

    def handle(self, *args, **kwargs):
        import this