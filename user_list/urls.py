from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from user_list.apiviews import AppUserCreate, AppUserDelete, TokenViewSet, AppUserInfo, AppUserUpdate

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet, basename='token')  # TODO: delete

urlpatterns = [
    path('list/', AppUserCreate.as_view(), name='list'),
    path('create/', AppUserCreate.as_view(), name='create'),
    path('info/<str:login>/', AppUserInfo.as_view(), name='info'),
    path('update/<str:login>/', AppUserUpdate.as_view(), name='update'),
    path('delete/<str:login>/', AppUserDelete.as_view(), name='delete'),
    url(r'^', include(router.urls))
]
