from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt

from .models import Users
from .models import Trips

def index(request):
    return HttpResponse('heck')

@csrf_exempt
def signup(request):
	email_in = request.POST.get('email')
	password_in = request.POST.get('password')

	try:
		user = Users(email=email_in, password=make_password(password_in))
		user.save()
		return HttpResponse(json.dumps({'success':user.id}, content_type='application/json'))
	except IntegrityError:
		raise Http404("email already in use")

@csrf_exempt
def login(request):
	email_in = request.POST.get('email')
	password_in = request.POST.get('password')

	print('WHAT ARE THE FIELDS {}'.format(request.POST))

	user = Users.objects.get(email = email_in)
	print('Does user exist? {}'.format(user))
	if not check_password(password_in, user.password):
		print('is this a 404?')
		raise Http404("password wrong")
	print('am i returning a response...')
	return HttpResponse(json.dumps({'success':user.id}, content_type='application/json'))

@csrf_exempt
def add_trip(request):
	user_id_in = request.POST.get('user')
	car_id_in = request.POST.get('car')
	start_lat_in = request.POST.get('start_lat')
	start_lon_in = request.POST.get('start_lon')
	city_in = request.POST.get('city')
	dist_traveled_in = request.POST.get('dist_traveled')
	dist_walked_in = request.POST.get('dist_walked')
	end_time_in = request.POST.get('end_time')
	duration_in = request.POST.get('duration')

	# trip = Trips(user_id = user_id_in, car_id = car_id_in, st)

@csrf_exempt
def fetch_user_trips(request):
	user_id_in = request.POST.get('user')

	user = Users.objects.get(id=user_id_in)
	user_trips = Trips.objects.filter(user_id = user.id)

	return HttpResponse(success)

@csrf_exempt
def fetch_comm_trips(request, lat_str_in, lon_str_in):
	latitude = float(request.POST.get('lat_str'))
	longitude = float(request.POST.get('lon_str'))

	success = latitude + longitude + + " successful fetch_comm_trips"
	return HttpResponse(success)







