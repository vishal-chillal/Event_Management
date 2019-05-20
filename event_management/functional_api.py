#!/bin/puthon
from event_management.models import UserInfo, EventDetails, CreatedEvents
import time
from django.db.models.query import QuerySet

class FunctionAPI(object):
    """docstring for FunctionAPI"""

    def __init__(self):
        self.user_details = UserInfo.objects.all()
        self.event_details = dict()
        self.counter = 0
        self.allEventList = list()

    def getAllEvents(self):
        ''' get all events avalable to show on dashboard '''
        self.counter += 1
        self.event_details = EventDetails.objects.all()
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

    def get_user_id(self, user_name):
        try:
            return UserInfo.objects.filter(user_name=user_name).values()[0]["id"]
        except Exception:
            return None
        
    def get_user_created_events(self, user_name):
        try:
            user_created_event_list = list()
            user_id = self.get_user_id(user_name)
            event_list = CreatedEvents.objects.filter(user_name_id=user_id).values()
            if not isinstance(event_list, QuerySet):
                event_list = [event_list] 

            for event in event_list:
                user_created_event_list.append(
                        self.get_event_details(event_id=event[0]))

            return user_created_event_list
        except UserInfo.DoesNotExist:
            return None


    def addEvent(self, req):
        ''' create event
            raise exception if unable to create event
        '''
        obj = EventDetails()
        obj.clean()
        obj.event_type = req["event_type"]
        obj.event_name = req["event_name"]
        obj.description = req["description"]
        obj.date_time = req["date_time"]
        obj.location = req["location"]
        obj.capacity = req["capacity"]
        obj.fees = req["fees"]
        try:
            obj.save()
            print("event_id", obj.id)
            return obj.id
        except Exception as e:
            print(e)
            raise

    def add_created_event_entry(self, user_name, event_id):
        user_details = self.get_user_details(user_name)
        event_details = self.get_event_details(event_id)
        try:
            print(event_details.date_time, user_details)
        except Exception as e:
            print(e.args[0],"eeee")
            raise
        try:
            obj = CreatedEvents()
            obj.user_name = user_details
            obj.id = event_details
            obj.save()
        except Exception as e:
            print(e.args[0],"rr")

    def get_event_details(self, event_id):
        try:
            return EventDetails.objects.get(id=event_id)
        except EventDetails.DoesNotExist:
            return None

    # def modify_user_event_list(self, user_name, event_id):
    #     user_details = self.get_user_details(user_name)
    #     try:
    #         interested_event_list = user_details.events_interested.split(",")
    #     except Exception:
    #         interested_event_list = []
    #     try:
    #         created_event_list = user_details.events_created.split(",")
    #     except Exception:
    #         created_event_list = []
    #     interested_event_list.append(str(event_id))
    #     created_event_list.append(str(event_id))
    #     try:
    #         print user_details.events_created

    #         user_details.events_created = ",".join(created_event_list)
    #         user_details.interested_created = ",".join(interested_event_list)
    #         user_details.save()
    #     except Exception as e:
    #         print "ERROR",e

    def getEventCapacity(self, eventid):
        return EventDetails.objects.filter(id=eventid).values()[0]["capacity"]

    def updateEventCapacity(self, decision, eventid):
        try:
            currentCapacity = self.getEventCapacity(eventid)
            currentCapacity += decision
            EventDetails.objects.filter(id=eventid).update(capacity=currentCapacity)
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
