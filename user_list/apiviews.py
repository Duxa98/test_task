from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route, action

from user_list.models import AppUser, Token
from .serializers import AppUserSerializer, TokenSerializer

from stories import Failure, Result, Success, arguments, story


class AppUserList(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserInfo(generics.RetrieveAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'


def load_object_pk(model, login):
    return model.objects.get(login=login).pk


def load_user_login(request):
    return request.data['login']


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
