# coding=utf-8
from django.contrib.auth import get_user_model
from django.db import models


class Sprint(models.Model):
    """
    A Spring
    """
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Point(models.Model):
    user = models.ForeignKey(get_user_model())
    sprint = models.ForeignKey(Sprint)

    velocity = models.IntegerField()
    scheduled = models.IntegerField()
    achieved = models.IntegerField()
    added = models.IntegerField()

    @property
    def overhead(self):
        return (self.scheduled + self.added) * 100 / self.scheduled - 100
