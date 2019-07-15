from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from user_list.apiviews import TokenViewSet, AppUserViewSet

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet, basename='token')
router.register(r'', AppUserViewSet, base_name='list')

urlpatterns = [
    url(r'^', include(router.urls))
]
