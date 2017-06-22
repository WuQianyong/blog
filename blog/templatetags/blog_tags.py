#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : blog_tags
# Fatures:
# Author : qianyong
# Time   : 2017-06-22 15:44
# Version: V0.0.1
#

from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates(
        'created_time','month',order='DESC'
    )

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()