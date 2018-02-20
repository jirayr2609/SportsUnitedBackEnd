from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

#This url returns all athletes
router.register(r'', AthleteViewSet, base_name='athletes')

#This url for anything regarding 1 athlete


urlpatterns = [
    url(r'^', include(router.urls)),
]