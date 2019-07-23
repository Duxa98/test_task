from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from user_list.apiviews import TokenViewSet, AppUserViewSet, UserCreate

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet, basename='token')
router.register(r'', AppUserViewSet, base_name='list')

urlpatterns = [
    path('create/', UserCreate.as_view(), name='user_create'),
    path('login/', views.obtain_auth_token, name='login'),
    url(r'^', include(router.urls)),
]
