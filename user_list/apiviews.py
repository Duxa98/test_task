# Create your views here.
from rest_framework import generics, viewsets

from user_list.models import AppUser, Token
from .serializers import AppUserSerializer, TokenSerializer


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'

    # def retrieve(self, request, *args, **kwargs):


class TokenViewSet(viewsets.ModelViewSet):
    # queryset = Token.objects.select_related('user').values(
    #     'user__login',
    #     'token',
    # )
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
