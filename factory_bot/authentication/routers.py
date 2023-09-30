from .viewsets import RegisterViewSet, UserTokenViewSet
from rest_framework.routers import DefaultRouter

def register_auth_router(router: DefaultRouter):
    router.register(r'register', RegisterViewSet, basename = 'register')
    router.register(r'token', UserTokenViewSet, basename='token')