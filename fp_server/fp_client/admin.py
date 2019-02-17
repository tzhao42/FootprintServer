from .models import Cars
from django.contrib import admin

# Register your models here.
class CarAdmin(admin.ModelAdmin):
	fields = ('name', 'emissions')

admin.site.register(Cars, CarAdmin)
