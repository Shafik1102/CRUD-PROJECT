from django.db import models
class Bike(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=65)
	colour=models.CharField(max_length=65)
	price=models.IntegerField()
	
