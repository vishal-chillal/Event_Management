from django.db import models
from datetime import datetime
# Create your models here.


class UserInfo(models.Model):
    '''class for user login '''
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    events_created = models.TextField(null=True)
    events_interested = models.TextField(null=True)

class Event(models.Model):
    '''docstring for Event'''
    class Meta:
        unique_together = (('event_type','location','date_time'),)
    id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(default=10)
    fees = models.IntegerField(default=0)