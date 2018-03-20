from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'', ContactViewSet, base_name='contactsporta'),


urlpatterns = [
    url(r'^', include(router.urls)),
]
