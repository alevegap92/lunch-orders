from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class FoodType(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.TextField(max_length=250, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	to_update = models.DateTimeField(auto_now=True)
	picture = models.ImageField(upload_to='foodtype', blank=True)
	price = models.IntegerField(default=0)

	foodselect = models.CharField(max_length=1,
		choices=(
		('m','MainDich'),
		('s','Salad'),
		('d','Desert')
	)
		,default='m')

	def __unicode__(self):
	    return self.name  

class Menu(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	menu = models.ManyToManyField(FoodType)
	menutime = models.TimeField()
	created = models.DateTimeField(auto_now_add=True)
	to_update = models.DateTimeField(auto_now=True)
	

class OrderMenu(models.Model):
 	customer = models.ForeignKey(User,on_delete=models.CASCADE)
 	menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
 	amount = models.IntegerField(default=0)
 	delivery = models.BooleanField(default=True)
 	ordertime = models.TimeField()
 	orderdate = models.DateTimeField(auto_now_add=True)

 	class meta:
 		ordering = ('-oderdate',)