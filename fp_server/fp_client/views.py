import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Users, Trips, Cars

def index(request):
    return HttpResponse('heck')

@csrf_exempt
def signup(request):
    email_in = request.POST.get('email')
    password_in = request.POST.get('password')
    
    try:
        user = Users(email=email_in, password=make_password(password_in))
        user.save()
        return HttpResponse(json.dumps({'user':user.id}), content_type='application/json')
    except IntegrityError:
         return HttpResponse(json.dumps({'error': 'That email is already taken'}), content_type='application/json')

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
    end_lat_in = float(request.POST.get('end_lat'))
    end_lon_in = float(request.POST.get('end_lon'))

    city_in = request.POST.get('city')
    dist_traveled_in = float(request.POST.get('dist_traveled'))
    dist_walked_in = float(request.POST.get('dist_walked'))
    end_time_in = datetime.strptime(request.POST.get('end_time'), '%b %d %Y %I:%M%p')
    print('successful')
    duration_in = float(request.POST.get('duration'))

    trip = Trips(user = user_in, car_id = car_id_in, start_lat = start_lat_in, start_lon = start_lon_in, end_lat = end_lat_in, end_lon = end_lon_in, city = city_in, dist_traveled = dist_traveled_in, dist_walked = dist_walked_in, end_time = end_time_in, duration = duration_in)
    trip.save()

    return HttpResponse(json.dumps({'trip':trip.id}), content_type='application/json')

@csrf_exempt
def fetch_user_trips(request):
    user_id_in = request.POST.get('user_id')

    user = Users.objects.get(id=user_id_in)
   # user_trips = list(user.trips_set.all())
    user_trips = list(Trips.objects.filter(user_id = user.id))
    user_trips_list_of_json = [ob.as_json() for ob in user_trips]
    return HttpResponse(json.dumps({'trips':user_trips_list_of_json}), content_type='application/json')

@csrf_exempt
def fetch_comm_trips(request):
    city_in = request.POST.get('city')

    city_trips = list(Trips.objects.filter(city = city_in))
    
    city_trips_list_of_json = [ob.as_json() for ob in city_trips]
    return HttpResponse(json.dumps({'trips':city_trips_list_of_json}), content_type='application/json')

@csrf_exempt
def stats(request):
    def carbonsaved(trip):
        walk = trip.dist_walked
        cs_factor = Cars.objects.get(id=trip.car_id).emissions
        return float(walk * cs_factor) #IN GRAMS PER MILE

    user_id_in = request.POST.get('user_id')
    try:
        user = Users.objects.get(id=user_id_in)
    except:
        return Http404('user doesnt exist lul')
    
    # savings for the last trip
    user_latest_trip = Trips.objects.filter(user=user).latest('end_time') # finds the latest trip
    
    user_carbonsaved_latest = carbonsaved(user_latest_trip)

    # cumulative savings
    user_trips = list(Trips.objects.filter(user_id = user.id))
    user_carbonsaved_cumulative_raw = 0
    for i in range(len(user_trips)):
        trip = user_trips[i]
        user_carbonsaved_cumulative_raw += carbonsaved(trip)
    user_carbonsaved_cumulative = float(user_carbonsaved_cumulative_raw / 1000) # KG
    #now we want to return user_carbonsaved_cumulative

    # savings for recent trips of nearby people
    user_city = user_latest_trip.city
    city_trips = list(Trips.objects.filter(city=user_city).order_by('-end_time'))
    city_trips_recent = city_trips[:25]
    city_trips_recent_highscores = sorted(city_trips_recent, key = carbonsaved)

    city_trips_recent_highscores_list_of_json = [ob.as_json() for ob in city_trips_recent_highscores]

    # return: user_carbonsaved_latest, user_carbonsaved_cumulative, city_trips_recent_highscores

    return HttpResponse(json.dumps({'latest': user_carbonsaved_latest, 'cumulative': user_carbonsaved_cumulative, 'city_trips_recent_highscores':city_trips_recent_highscores_list_of_json}), content_type='application/json')