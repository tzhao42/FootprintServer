from .models import Cars, Trips
from django.contrib import admin

# Register your models here.
class CarAdmin(admin.ModelAdmin):
	fields = ('name', 'emissions')

class TripAdmin(admin.ModelAdmin):
	fields = ('user', 'car_id', 'city', 'end_time', 'dist_traveled', 'dist_walked')

admin.site.register(Cars, CarAdmin)
admin.site.register(Trips, TripAdmin)