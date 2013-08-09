# coding=utf-8
"""
Urls
"""

from django.conf.urls import patterns
import sprints.views

urlpatterns = patterns('',
                       (r'^users/$', sprints.views.get_all),
                       (r'^users/(?P<user_id>\d)/$', sprints.views.get_one)
)
