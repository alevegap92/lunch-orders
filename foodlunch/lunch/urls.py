from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .views import *
#from lunch import views

urlpatterns = [

	url(r'^menu$', ListMenu.as_view(),name="list_menu"),
    url(r'^menu/create/$', staff_member_required(CreateMenu.as_view()), name="create_menu"),
    url(r'^menu/update/(?P<pk>.+)$', staff_member_required(UpdateFoodType.as_view()), name="update_menu"),
    url(r'^menu/foodtype/(?P<pk>.+)$',DetailMenu.as_view(), name="detail_menu"),
    url(r'^menu/delete/(?P<pk>.+)$', staff_member_required(DeleteMenu.as_view()), name="delete_menu"),


    url(r'^food$', ListFoodType.as_view(), name="list_foodtype"),
    url(r'^create/$', staff_member_required(CreateFoodType.as_view()), name="create_foodtype"),
    url(r'^update/(?P<pk>.+)$', staff_member_required(UpdateFoodType.as_view()), name="update_foodtype"),
    url(r'^foodtype/(?P<pk>.+)$',DetailFoodType.as_view(), name="detail_foodtype"),
    url(r'^delete/(?P<pk>.+)$', staff_member_required(DeleteFoodType.as_view()), name="delete_foodtype"),
]
