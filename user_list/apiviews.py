# Create your views here.
from rest_framework import generics, viewsets

from user_list.models import AppUser, Token
from .serializers import AppUserSerializer, TokenSerializer


class AppUserList(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserInfo(generics.RetrieveAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'


class AppUserCreate(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'


class AppUserDelete(generics.RetrieveDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'


class TokenViewSet(viewsets.ModelViewSet):
    # queryset = Token.objects.select_related('user').values(
    #     'user__login',
    #     'token',
    # )
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
