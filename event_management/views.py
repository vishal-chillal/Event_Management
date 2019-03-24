from django.http import HttpResponse
import ast

from functional_api import FunctionAPI

func = FunctionAPI()


def index(request):
    print(dir(request))
    if request.path == '/event/':
        return HttpResponse("<h2>Hello.. Welcome to Event Management.</h2>")
    else:
        return HttpResponse("<h3>Hello.. Welcome to django projects</h3>")


def all_event_list(request):
    return func.generateAllEventList()


def dashboard(request):
    """This will be the dashboard of event management system"""
    return HttpResponse(str(func.getAllEvents()))


def event(request):
    ''' admin panal handle event request '''
    # if request.method == "GET":
    #     if 'username' in request.session:
    #         html = func.generateAllEventList()
    #         return HttpResponse(html)
    #     else:
    #         return HttpResponse("INVALID")
    if request.method == "GET":
        html = func.generateAllEventList()
        return HttpResponse(html)

    elif request.method == "POST":
        data = ast.literal_eval(request.body)
        print data
        if func.addEvent(data):
            return HttpResponse("Success", 202)
        else:
            return HttpResponse("Fail", 400)
