# coding=utf-8
"""
Views
"""
from django.shortcuts import render_to_response
from sprints.models import Point


def get_all(request):
    """
    Get all users
    """
    points = Point.objects.all()  # group by users, get the names as well
    return render_to_response('sprints/users.html', {'points': points})


def get_one(request, user_id):
    """
    Get one user
    """
    points = Point.objects.all()  # group by users, get the names as well
    return render_to_response('sprints/users.html', {'points': points})


def get_group(request, group_id):
    """
    Get a group
    """
    pass
