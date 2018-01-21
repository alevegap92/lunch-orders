from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	list_display = ('menu_name', 'created', 'to_update')
	search_fields = ('menu_name','created')
	list_filter = ('created',)

class FoodTypeAdmin(admin.ModelAdmin):
	list_display = ('foodselect','name','price', 'created', 'to_update')
	search_fields = ('name','price','created')
	list_filter = ('foodselect','created',)

admin.site.register(FoodType,FoodTypeAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(OrderMenu)
