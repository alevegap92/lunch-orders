from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^food$', ListFoodType.as_view(), name="list_foodtype"),
    url(r'^create/$', staff_member_required(CreateFoodType.as_view()), name="create_foodtype"),
    url(r'^(?P<pk>.+)/update/$', staff_member_required(UpdateFoodType.as_view()), name="update_foodtype"),
    url(r'^(?P<pk>.+)/foodtype/$',DetailFoodType.as_view(), name="detail_foodtype"),
    url(r'^(?P<pk>.+)/delete/$', staff_member_required(DeleteFoodType.as_view()), name="delete_foodtype"),
]
