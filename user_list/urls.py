from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from user_list.apiviews import AppUserCreate, AppUserViewSet, AppUserDelete, AppUserListView, TokenViewSet

router = routers.DefaultRouter()
# router.register(r'list', AppUserListView, basename='list')
router.register(r'tokens', TokenViewSet, basename='token') #TODO: delete
router.register(r'list', AppUserViewSet, basename='list')
router.register(r'info', AppUserViewSet, basename='info')
router.register(r'create', AppUserViewSet, basename='create')

urlpatterns = [
    # path('create/', AppUserCreate.as_view(), name='user_create'),
    path('<str:login>/delete', AppUserDelete.as_view(), name='user_del'),
    url(r'^', include(router.urls))
]