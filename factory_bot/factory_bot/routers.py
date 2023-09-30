from rest_framework.routers import DefaultRouter
from authentication.routers import register_auth_router
from messages_bot.routers import register_messages_router

router = DefaultRouter()
register_auth_router(router)
register_messages_router(router)
