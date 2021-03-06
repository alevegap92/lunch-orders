from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import uuid
# Create your models here.
@python_2_unicode_compatible
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
		('d','Dessert')
	)
		,default='m')

	def __str__(self):
	    return self.name  

@python_2_unicode_compatible
class Menu(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	menu_name = models.CharField(max_length=50, unique=True)
	menu_foodtype = models.ManyToManyField(FoodType)
	created = models.DateTimeField(auto_now_add=True)
	to_update = models.DateTimeField(auto_now=True)
	def __str__(self):
	    return self.menu_name 
	     	
@python_2_unicode_compatible
class OrderMenu(models.Model):
 	customer = models.ForeignKey(User,on_delete=models.CASCADE)
 	menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
 	amount = models.IntegerField(default=0)
 	delivery = models.BooleanField(default=True)
 	orderdate = models.DateTimeField(auto_now_add=True)

 	class meta:
 		ordering = ('-oderdate',)

 	def __str__(self):
	    return self.customer.username
