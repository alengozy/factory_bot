from .viewsets import MessagesViewSet

def register_messages_router(router):
    router.register(r'messages', MessagesViewSet, basename = 'messages')