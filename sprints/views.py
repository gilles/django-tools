# coding=utf-8
"""
Views
"""
from collections import defaultdict
from django.shortcuts import render
from sprints.models import Point


def get_user_data(user_id):
    if user_id:
        points = Point.objects.select_related().filter(user__id=user_id)
    else:
        points = Point.objects.select_related().all().order_by('user__id', '-sprint__id')

    # this dict kind of kills the order, use an orderedict and handle default.
    # Or write a complicated class. (might work with mixins, to try)
    # or just use templates regroup/dictsort
    view = defaultdict(list)
    for point in points:
        view[point.user.username].append(point)
    view = dict(view)
    return view


def get_all(request):
    """
    Get all users
    """
    view = get_user_data(None)
    return render(request, 'sprints/users.html', {'view': view})


def get_one(request, user_id):
    """
    Get one user
    """
    view = get_user_data(user_id)
    return render(request, 'sprints/users.html', {'view': view})


def get_group(request, group_id):
    """
    Get a group. Need the concept of a group first
    """
    pass
