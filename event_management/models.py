from django.db import models

# Create your models here.


class UserInfo(models.Model):
    '''class for user login '''
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Event(models.Model):
    '''docstring for Event'''
    eventname = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    # startdate = models.DateTimeField()
    # enddate = models.DateTimeField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    fees = models.IntegerField()
    # info = models.CharField(max_length=100)
