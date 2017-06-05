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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from protoapp.views import \
    (AboutView, ContactView, CryptView, HomeView, LipsumView, SessionView)

urlpatterns = [
    url(r'^$',                          HomeView.as_view()),
    url(r'^about/$',                    AboutView.as_view()),
    url(r'^admin/',                     admin.site.urls),
    url(r'^api/',                       include('api.urls')),
    url(r'^crypt/$',                    CryptView.as_view()),
    url(r'^crypt/(?P<rounds>[0-9]+)/$', CryptView.as_view()),
    url(r'^contact/$',                  ContactView.as_view()),
    url(r'^lipsum/$',                   LipsumView.as_view()),
    url(r'^session/$',                  SessionView.as_view()),
    url(r'^static/(?P<path>.*)$',       serve,
            { 'document_root': settings.STATIC_ROOT }),
]
