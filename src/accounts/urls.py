from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'sportaregistration', SportaRegistrationViewSet, base_name='sportaregistration'),

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^registration/$', CustomRegisterView.as_view(), name='rest_custom_register'),
    
    # url(r'^load-user/$', CustomLoadUserView.as_view(), name='rest_custom_load_user'),
    # url(r'^verify-user/$', CustomVerifyEmail.as_view(), name='rest_custom_verify_email'),
    # url(r'^logout/$', Logout.as_view(), name='rest_account_logout'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]