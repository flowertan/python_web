# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/11/17 20:54
# @file    : urls.py
# @desc    : blog.urls
#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]