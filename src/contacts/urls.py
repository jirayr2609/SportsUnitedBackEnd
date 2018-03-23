from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'', ContactRegistrationViewSet, base_name='contactregistration'),


urlpatterns = [
    url(r'^', include(router.urls)),
]
