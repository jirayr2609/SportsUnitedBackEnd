"""sportsunited URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    # Main BackEnd routes
    path('admin/', admin.site.urls),
    url(r'^api/sporta/accounts/', include('accounts.urls'), name='accounts-url'), # email confirmation.
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')), # Basic registration goes through here
    url(r'^api/sporta/contacts/', include('contacts.urls'), name='contacts-url'),
    # Other routes that may require implementation in the future
    url(r'^account/', include('allauth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),

    url(r'^api/sporta/athletes/', include('athletes.urls'), name='athletes-url'),
    url(r'^api/sporta/teams/', include('teams.urls'), name='teams-url'),
    url(r'^api/sporta/leagues/', include('leagues.urls'), name='leagues-url')
]



    # url(r'^api/v1/', include('authentication.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^photologue/', include('photologue.urls', namespace='photologue')),
