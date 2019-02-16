from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
#from . import models
from .models import Users
from .models import Trips

def index(request):
    return HttpResponse('heck')

def signup(request, email_in, password_in):
	try:
		user = Users(email=email_in, password=make_password(password_in))
		user.save()
		success= user.email + " signup successful"
		return HttpResponse(success)
	except IntegrityError:
		raise Http404("email already in use")

def login(request, email_in, password_in):
	user = Users.objects.get(email = email_in)
	if not check_password(password_in, user.password):
		raise Http404("password wrong")
	return HttpResponse("login successful for " + user.email)

def fetch_user_trips(request, user_id_in):
	user = Users.objects.get(id=user_id_in)
	success= user.email + " successful fetch_user_trips"
	return HttpResponse(success)

def fetch_comm_trips(request, lat_str_in, long_str_in):
	latitude = float(lat_str)
	longitude = float(long_str)
	success=latitude + longitude + + " successful fetch_comm_trips"
	return HttpResponse(sucess)