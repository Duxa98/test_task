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


class AppUserDelete(generics.DestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'login'
