from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from user_list.apiviews import AppUserCreate, AppUserList, AppUserInfo, AppUserModify, AppUserDelete

router = routers.DefaultRouter()
router.register(r'list', AppUserList, basename='list')

urlpatterns = [
    path('create/', AppUserCreate.as_view(), name='user_create'),
    path('info/<str:login>/', AppUserInfo.as_view(), name='user_info'),
    path('modify/<str:login>/', AppUserModify.as_view(), name='user_modify'),
    path('delete/<str:login>', AppUserDelete.as_view(), name='user_del'),
]

urlpatterns += router.urls