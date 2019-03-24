"""myblog URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import  url
from myblogs import views
urlpatterns = [
    url(r'^index', views.index),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^register$', views.register),
    url(r'^register2$', views.register2),
    url(r'^detail(?P<num>\d+)$', views.detail),
    url(r'^center(?P<username>\w+)$', views.center),
    url(r'^center$', views.login),
    url(r'^create_contention$', views.create_contention),

    url(r'^create$', views.create),
    url(r'^logout$',views.logout),
]
