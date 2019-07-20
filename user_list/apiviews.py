# Create your views here.
from rest_framework import viewsets

from user_list.models import AppUser, Token
from .serializers import AppUserSerializer, TokenSerializer, AppUserInfoSerializer


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    lookup_field = 'login'

    def get_serializer_class(self):
        if self.action in ('retrieve', 'update', 'partial_update'):
            return AppUserInfoSerializer
        return AppUserSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
