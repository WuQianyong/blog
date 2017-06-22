#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : urls
# Fatures:
# Author : qianyong
# Time   : 2017-06-22 10:00
# Version: V0.0.1
#

from django.conf.urls import  url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
]