from event_management.models import UserInfo, Event
import time


class FunctionAPI(object):
    """docstring for FunctionAPI"""

    def __init__(self):
        self.user_details = UserInfo.objects.values()
        self.event_details = {}
        self.allEventList = {}
        self.counter = 0

    def cleanJson(self, request):
        ''' get the request body and convert it into clean json '''
        ls = request.split('&')
        dic = {}
        for x in ls:
            dic[x.split('=')[0]] = x.split('=')[1]
        return dic

    def getAllEvents(self):
        ''' get  all events avalable to subscribe '''
        self.counter += 1
        self.event_details = Event.objects.values()
        for eachevent in self.event_details:
            self.allEventList[eachevent["id"]] = eachevent["eventname"]
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
        obj.id = int(time.time())
        obj.capacity = req.get("capacity",None)
        obj.description = req.get("description",None)
        obj.eventname = req.get("eventname",None)
        obj.location = req.get("location",None)
        obj.fees = req.get("fees",None)
        obj.startdate = req.get("startdate",None)
        obj.enddate = req.get("enddate",None)
        obj.info = req.get("info",None)
        try:
            obj.save()
            return True
        except Exception as e:
            print e
            return False

    def getEventCapacity(self, eventid):
        return Event.objects.filter(id=eventid).values()[0]["capacity"]

    def updateEventCapacity(self, decision, eventid):
        try:
            currentCapacity = self.getEventCapacity(eventid)
            currentCapacity += decision
            Event.objects.filter(id=eventid).update(capacity=currentCapacity)
            return True
        except Exception as e:
            print e
            return False

    # def getMyEvents(self, username):
    #     query = """SELECT * from krishi_subscription where username = """
    #     query += "'" + username + "'"
    #     self.myEventList = {}

    #     event_lst = Subscription.objects.raw(query)
    #     for eachEvnt in event_lst:
    #         value = self.allEventList[eachEvnt.eventid]
    #         self.myEventList[eachEvnt.eventid] = value
    #     print self.myEventList, " ", username
    #     return self.myEventList

    def generateAllEventList(self):
        html = '<h1>All Events</h1><br><div>'
        allevents = self.getAllEvents()
        for each in allevents.items():
            html += "<a href="
            url_name = str(each[0])
            html += url_name + ">"
            html += str(each[1]) + "</a><br>"
        html += '</div><br>'
        return html
