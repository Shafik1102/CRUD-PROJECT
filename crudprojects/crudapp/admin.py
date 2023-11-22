from django.contrib import admin
from crudapp.models import Bike
class BikeAdmin(admin.ModelAdmin):
	list_display=['no','name','colour','price']
admin.site.register(Bike,BikeAdmin)
