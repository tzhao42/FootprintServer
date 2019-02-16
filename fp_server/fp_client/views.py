import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Users
from .models import Trips

def index(request):
    return HttpResponse('heck')

@csrf_exempt
def signup(request):
    email_in = request.POST.get('email')
    password_in = request.POST.get('password')
    print("REQUEST BODY {}".format(request.POST))
    
    print("email_in is {} password_in is {}".format(email_in, password_in))
    user = Users(email=email_in, password=make_password(password_in))
    user.save()
    return HttpResponse(json.dumps({'user':user.id}), content_type='application/json')

@csrf_exempt
def login(request):
    email_in = request.POST.get('email')
    password_in = request.POST.get('password')

    user = Users.objects.get(email = email_in)
	
    if not check_password(password_in, user.password):
        return HttpResponse(json.dumps({'error': 'The password is incorrect'}), content_type='application/json')
    return HttpResponse(json.dumps({'user': user.id}), content_type='application/json')

@csrf_exempt
def add_trip(request):
    user_id_in = int(request.POST.get('user_id'))
    user_in = Users.objects.get(id=user_id_in)
    
    car_id_in = int(request.POST.get('car_id'))
    start_lat_in = float(request.POST.get('start_lat'))
    start_lon_in = float(request.POST.get('start_lon'))
    city_in = request.POST.get('city')
    dist_traveled_in = float(request.POST.get('dist_traveled'))
    dist_walked_in = float(request.POST.get('dist_walked'))
    end_time_in = datetime.strptime(request.POST.get('end_time'), '%b %d %Y %I:%M%p')
    print('successful')
    duration_in = float(request.POST.get('duration'))

    trip = Trips(user = user_in, car_id = car_id_in, start_lat = start_lat_in, start_lon = start_lon_in, city = city_in, dist_traveled = dist_traveled_in, dist_walked = dist_walked_in, end_time = end_time_in, duration = duration_in)
    trip.save()

    return HttpResponse(json.dumps({'trip':trip.id}), content_type='application/json')

@csrf_exempt
def fetch_user_trips(request):
    user_id_in = request.POST.get('user_id')

    user = Users.objects.get(id=user_id_in)
   # user_trips = list(user.trips_set.all())
    user_trips = list(Trips.objects.filter(user_id = user.id))
    return HttpResponse(json.dumps({'trips':user_trips}), content_type='application/json')

@csrf_exempt
def fetch_comm_trips(request):
    city_in = request.POST.get('city')

    city_trips = list(Trips.objects.filter(city = city_in))

    return HttpResponse(json.dumps({'trips':city_trips}), content_type='application/json')
