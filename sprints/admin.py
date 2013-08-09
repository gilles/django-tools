# coding=utf-8
"""
Admin
"""
from django.contrib import admin
from sprints.models import Sprint, Point


class SprintAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    # fields = ('start_date', 'end_date', 'name')
    list_display = ('name', 'start_date', 'end_date')


admin.site.register(Sprint, SprintAdmin)


class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'sprint', 'scheduled', 'achieved')


admin.site.register(Point, PointAdmin)
