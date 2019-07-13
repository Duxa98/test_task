from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route, action

from user_list.models import AppUser, Token
from .serializers import AppUserSerializer, TokenSerializer

from stories import Failure, Result, Success, arguments, story


class AppUserListView(viewsets.ModelViewSet):

    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserViewSet(viewsets.ModelViewSet):

    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'

    # def create(self, request, *args, **kwargs):
    #
    #     resp = super(AppUserViewSet, self).create(self, request, *args, **kwargs)
    #
    #     print(resp)
    #
    #     return resp

# class AppUserCreateViewSet(mixins.CreateModelMixin, viewsets.ModelViewSet):
    # def post(self):


class AppUserCreate(generics.ListCreateAPIView):
    queryset = AppUser.objects.all().order_by('login')
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        user = super(AppUserCreate, self).create(request, *args, **kwargs)

        login = request.data['login']
        user_id = AppUser.objects.get(login=login).pk

        Token.objects.create(
            token=f'{login}_token',
            user_id=user_id
        )

        return user


class TokenViewSet(viewsets.ModelViewSet):
    # queryset = Token.objects.select_related('user').values(
    #     'user__login',
    #     'token',
    # )
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class AppUserDelete(generics.DestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'
