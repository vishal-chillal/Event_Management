from django.db import models
from datetime import datetime
# Create your models here.


class UserInfo(models.Model):
    '''class for user login '''
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class EventDetails(models.Model):
    '''docstring for Event'''
    id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=100, null=False)
    event_name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=800)
    date_time = models.DateTimeField(default=datetime.now, null=False)
    location = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(default=10)
    fees = models.IntegerField(default=1)


class CreatedEvents(models.Model):
    '''class to identofy events created by users'''
    user_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    event_id = models.OneToOneField(EventDetails, on_delete=models.CASCADE, primary_key=True)
