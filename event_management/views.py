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

def login_user(request):
    if request.method == "POST":
        data = ast.literal_eval(request.body)
        print "login_request",data
        return HttpResponse("Success", status='200')
    else:
        return HttpResponse('Error', status='404')

def register(request):
    ''' handle registration of users '''
    if request.method == "POST":
        """convert the request to simple dict format"""
        data = ast.literal_eval(request.body)


        """handle empty fields and send error code"""
        # yet to be handled 


        user = data.get('user_name')
        """get all user list from database and validate presence of user"""
        user_list = func.get_all_users()
        print user_list
        if user_list:
            if user in user_list :
                return HttpResponse('Error', status='404')

        """add new entry to the database and send success report"""
        func.add_user_details(data)
        return HttpResponse("Success", status='200')
            
    if request.method == "GET":
        html = func.generateAllEventList()
        return HttpResponse(html)
