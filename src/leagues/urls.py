from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

#This url returns leagues
router.register(r'leagues', LeagueViewSet, base_name='leagues'),
#This url returns divisions 
router.register(r'divisions', LeagueDivisionViewSet, base_name='leagues_divisions')

urlpatterns = [
    url(r'^', include(router.urls)),
]