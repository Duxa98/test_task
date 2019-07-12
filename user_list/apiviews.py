from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user_list.models import AppUser
from .serializers import AppUserSerializer


class AppUserList(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserInfo(generics.RetrieveAPIView):

    def get_object(self):
        object = AppUser.objects.get(login=self.kwargs['login'])
        return object

    serializer_class = AppUserSerializer


class AppUserCreate(generics.ListCreateAPIView):
    serializer_class = AppUserSerializer


class AppUserModify(generics.RetrieveUpdateAPIView):
    pass


class AppUserDelete(generics.RetrieveDestroyAPIView):
    pass
