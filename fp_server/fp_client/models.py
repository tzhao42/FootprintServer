from django.db import models

class Users(models.Model):
	email=models.CharField(max_length=200, unique=True)
	password=models.CharField(max_length=200)

class Cars(models.Model):
	name=models.CharField(max_length=200)
	emissions=models.FloatField(max_length=20)

class Trips(models.Model):

	user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
	car_id=models.IntegerField(Cars)

	start_lat=models.FloatField(max_length=20)
	start_lon=models.FloatField(max_length=20)

	city=models.CharField(max_length=200)

	dist_traveled=models.FloatField(max_length=20)
	dist_walked=models.FloatField(max_length=20)

	end_time=models.DateTimeField()
	duration=models.FloatField(max_length=20)
