"""SITW_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^musicAPP/',	include('musicAPP.urls',	namespace='musicapp')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('musicapp:home_page'), permanent=True)),

    # User login: /accounts/login
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),

    # User logout: /accounts/logout
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/musicAPP'}),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
