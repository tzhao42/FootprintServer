from django.db import models
from datetime import datetime

class Users(models.Model):
    email=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=200)

class Cars(models.Model):
    name=models.CharField(max_length=200)
    emissions=models.FloatField(max_length=20)

class Trips(models.Model):

    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    car_id=models.IntegerField()

    start_lat=models.FloatField(max_length=20)
    start_lon=models.FloatField(max_length=20)

    end_lat=models.FloatField(max_length=20)
    end_lon=models.FloatField(max_length=20)

    city=models.CharField(max_length=200)

    dist_traveled=models.FloatField(max_length=20)
    dist_walked=models.FloatField(max_length=20)

    end_time=models.DateTimeField()
    duration=models.FloatField(max_length=20)

    def as_json(self):
        return dict(
            user_id = self.user.id,
            car_id = self.car_id,
            start_lat = self.start_lat,
            start_lon = self.start_lon,
            city = self.city,
            dist_traveled = self.dist_traveled,
            dist_walked = self.dist_walked,
            end_time = (self.end_time).strftime('%Y-%m-%d %H:%M:%S'),
            duration = self.duration
            )
