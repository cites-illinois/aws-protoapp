"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router_dict = \
    {
    r'author'   : views.AuthorViewSet,
    r'groups'   : views.GroupViewSet,
    r'quote'    : views.QuoteViewSet,
    r'users'    : views.UserViewSet,
    }

for pattern, view in router_dict.items():
    router.register(pattern, view)

urlpatterns = \
    [
    url(r'^',           include(router.urls)),
    url(r'^api-auth/',  include('rest_framework.urls')),
    ]
