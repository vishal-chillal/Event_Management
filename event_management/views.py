from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView  # Import TemplateView
from functional_api import FunctionAPI
import ast
import json
import datetime
import pytz
func = FunctionAPI()


def redirect_view(request):
    response = redirect('/event/signup')
    return response


class SignupPageView(TemplateView):
    template_name = "signup.html"


class SigninPageView(TemplateView):
    template_name = "signin.html"


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"


def login_user(request):
    if request.method == "POST":
        print(request.body)
        data = ast.literal_eval(request.body)
        user = data.get('user_name')
        user_details = func.get_user_details(user)
        if user_details and user_details.password == data.get('password'):
            return HttpResponse("Success", status='200')
        else:
            return HttpResponse('Error', status='403')
    else:
        return HttpResponse('Error', status='404')


def register_user(request):
    ''' handle registration of users '''
    if request.method == "POST":
        """convert the request to simple dict format"""
        data = ast.literal_eval(request.body)
        try:
            user = data['user_name']
        except KeyError:
            return HttpResponse('Error', status='409')
        """get all user list from database and validate presence of user"""
        user_list = func.get_all_users()
        if user_list:
            if user in user_list:
                return HttpResponse('Error', status='409')

        """add new entry to the database and send success report"""
        func.add_user_details(data)
        return HttpResponse("Success", status='201')


def dashboard(request):
    ''' handle registration of users '''
    if request.method == "POST":
        return HttpResponse("Success", status='201')
    else:
        return HttpResponse("Success", status='201')


def events(request, user=""):
    ''' handle CURD opetration on events '''
    if request.method.upper() == "POST":
        data = ast.literal_eval(request.body)
        request_data = dict()
        try:
            request_data['event_type'] = data["event_type"]
            request_data['event_name'] = data["event_name"]
            request_data['location'] = data["location"]
            request_data['date_time'] = data["event_date"]
            event_time = data["time"]
            event_date = request_data['date_time'] + " " + event_time
            
            date_format = '%Y-%m-%d %I:%M'

            unaware_start_date = datetime.datetime.strptime(event_date, date_format)
            request_data['date_time'] = pytz.utc.localize(unaware_start_date)

            print(request_data['date_time'], event_time)
            if data.has_key("capacity"):
                request_data['capacity'] = data["capacity"]
            if data.has_key("description"):
                request_data['description'] = data["description"]
            if data.has_key("fees"):
                request_data['fees'] = data["fees"]
        except KeyError as E:
            resp_msg = E.args[0] + " is not given in the request"
            return HttpResponse(resp_msg, status='400')
        try:
            event_id = func.addEvent(request_data)
            if event_id:
                func.add_created_event_entry(user_name=data['user_name'],
                                             event_id=event_id)
                return HttpResponse("Success", status='201')
            else:
                raise Exception("Error")
        except Exception as e:
            return HttpResponse(e.args[0], status='400')

    elif request.method.upper() == "GET":
        all_events = func.getAllEvents()
        user_name = str(request.GET['user_name'])
        user_created_events = func.get_user_created_events(user_name)
        response = dict()
        response["all_events"] = all_events
        response['user_created_events'] = user_created_events
        return HttpResponse(json.dumps(response), status='200')
