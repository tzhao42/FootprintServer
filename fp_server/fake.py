import random
import datetime
import math as m

from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError

from fp_client.models import Users, Trips, Cars

def get_rand_lat():
		seed = random.random()*10-5
		seed += 38.6270
		return seed

def get_rand_lon():
	seed = random.random()*10-5
	seed += 90.1994
	return seed

def get_rand_car_id():
	# 1,2,3,4,5,6,7,8,9,10,11
	seed = random.random()
	return int(m.floor(seed*10)+1)

def get_rand_dist_walked(): # in miles
	#from 0 to 2 miles
	return random.random()*2

def get_dist_traveled(start_lat, start_lon, end_lat, end_lon): # in miles
	RADIUS = 3959 # radius of the earth is 3959 miles
	arg1 = m.radians((start_lat - end_lat)/2)
	arg2 = m.radians(start_lat)
	arg3 = m.radians(end_lat)
	arg4 = m.radians((start_lon - end_lon)/2)

	d= 2*RADIUS * m.asin(m.sqrt((m.sin(arg1))**2+m.cos(arg2)*m.cos(arg3)*(m.sin(arg4))**2))
	return d

def get_rand_duration(dist_traveled): # in seconds
	speed = random.random()*30+40 # in mph
	time = dist_traveled/speed #in hours
	return int(m.floor(time*60*60))

def get_rand_datetime(year=2019):
	try:
		return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')
	except ValueError:
		get_random_date(year)

def main():
	NUM_FAKE_TRIPS = 20
	# try:
	#	fake_user = Users(email='FAKEUSER', password=make_password('FAKEPASSWORD'))
	#	fake_user.save()
	# except:
	#	print("already made this user, skipping this step")

	fake_user = Users.objects.get(id=7)

	for i in range(NUM_FAKE_TRIPS):
		user=fake_user

		car_id= get_rand_car_id()
		start_lat= get_rand_lat()
		start_lon= get_rand_lon()
		end_lat= get_rand_lat()
		end_lon= get_rand_lon()
		city="St. Louis"
		dist_traveled= get_dist_traveled(start_lat, start_lon, end_lat, end_lon)
		dist_walked= get_rand_dist_walked()
		end_time= get_rand_datetime()
		duration= get_rand_duration(dist_traveled)

		t=Trips(user = user, car_id = car_id, start_lat = start_lat, start_lon = start_lon, end_lat = end_lat, end_lon = end_lon, city = city, dist_traveled = dist_traveled, dist_walked = dist_walked, end_time = end_time, duration = duration)
		t.save()

if __name__ == "__main__":
	main()
	