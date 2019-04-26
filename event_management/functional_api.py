#!/bin/puthon
from event_management.models import UserInfo, Event
import time


class FunctionAPI(object):
    """docstring for FunctionAPI"""

    def __init__(self):
        self.user_details = UserInfo.objects.all()
        self.event_details = dict()
        self.counter = 0
        self.allEventList = list()

    def cleanJson(self, request):
        ''' get the request body and convert it into clean json '''
        ls = request.split('&')
        dic = {}
        for x in ls:
            dic[x.split('=')[0]] = x.split('=')[1]
        return dic

    def getAllEvents(self):
        ''' get all events avalable to subscribe '''
        self.counter += 1
        self.event_details = Event.objects.all()
        self.allEventList = list()

        for eachevent in self.event_details:
            self.allEventList.append({
                "id": eachevent.id,
                "event_name": eachevent.event_name,
                "location": eachevent.location,
                "capacity": eachevent.capacity,
                "date_time": eachevent.date_time.strftime("%Y-%m-%d %H:%M:%S"),
                "event_type": eachevent.event_type
            })
        return self.allEventList

    def getEvent(self, id):
        res = {}
        for eachevent in self.event_details:
            if str(eachevent["id"]) == str(id):
                res = eachevent
                break
        return res

    def addEvent(self, req):
        obj = Event()
        obj.event_type = req["event_type"]
        obj.event_name = req["event_name"]
        obj.description = req["description"]
        obj.date_time = req["date_time"]
        obj.location = req["location"]
        obj.capacity = req["capacity"]
        obj.fees = req["fees"]
        try:
            obj.save()
            return True
        except Exception:
            raise

    def getEventCapacity(self, eventid):
        return Event.objects.filter(id=eventid).values()[0]["capacity"]

    def updateEventCapacity(self, decision, eventid):
        try:
            currentCapacity = self.getEventCapacity(eventid)
            currentCapacity += decision
            Event.objects.filter(id=eventid).update(capacity=currentCapacity)
            return True
        except Exception as e:
            print(e)
            return False

    def get_user_details(self, user):
        try:
            return UserInfo.objects.get(user_name=user)
        except UserInfo.DoesNotExist:
            return None

    def get_all_users(self):
        return map(lambda x: x.user_name, self.user_details)

    def add_user_details(self, user_dict):
        user = UserInfo()
        user.user_name = user_dict['user_name']
        user.password = user_dict['password']
        user.email = user_dict['email']
        user.save()
