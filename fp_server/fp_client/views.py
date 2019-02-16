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
	print('calling signup')
	# print('email is {} password is {}'.format(email, password))

	try:
		user = Users(email=email_in, password=make_password(password_in))
		user.save()
		success= user.email + " signup successful"
		return HttpResponse(success)
	except IntegrityError:
		raise Http404("email already in use")

@csrf_exempt
def login(request):
	email_in = request.POST.get('email')
	password_in = request.POST.get('password')

	user = Users.objects.get(email = email_in)
	if not check_password(password_in, user.password):
		raise Http404("password wrong")
	return HttpResponse("login successful for " + user.email)

@csrf_exempt
def fetch_user_trips(request):
	user_id_in = request.POST.get('user')

	user = Users.objects.get(id=user_id_in)
	success= user.email + " successful fetch_user_trips"
	return HttpResponse(success)

@csrf_exempt
def fetch_comm_trips(request, lat_str_in, long_str_in):
	latitude = float(request.POST.get('lat_str'))
	longitude = float(request.POST.get('long_str'))

	success = latitude + longitude + + " successful fetch_comm_trips"
	return HttpResponse(sucess)







