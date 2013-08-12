# coding=utf-8
"""
Urls
"""

from django.conf.urls import patterns, url
import sprints.views

urlpatterns = patterns('',
                       url(r'^users/$', sprints.views.get_all, name='users-list'),
                       url(r'^users/(?P<user_id>\d)/$', sprints.views.get_one, name='users-detail')
)
