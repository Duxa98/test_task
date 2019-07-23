# Create your views here.
from rest_framework import viewsets, generics

from user_list.models import AppUser, MyToken
from .serializers import AppUserSerializer, MyTokenSerializer, AppUserInfoSerializer, UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    lookup_field = 'login'

    def get_serializer_class(self):
        if self.action in ('retrieve', 'update', 'partial_update'):
            return AppUserInfoSerializer
        return AppUserSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = MyToken.objects.all()
    serializer_class = MyTokenSerializer
