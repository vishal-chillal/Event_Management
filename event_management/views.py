from django.http import HttpResponse
from django.shortcuts import render
import ast
from django.views.generic import TemplateView # Import TemplateView

from functional_api import FunctionAPI

func = FunctionAPI()

class SignupPageView(TemplateView):
    template_name = "signup.html"


class SigninPageView(TemplateView):
    template_name = "signin.html"


def register_user(request):
    if request.method == "POST":
        if 'username' in request.session:
            html = func.generateAllEventList()
            return HttpResponse(html)
        else:
            return request
    elif request.method == "GET":
        return HttpResponse(request.method)

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
        return HttpResponse("Success")