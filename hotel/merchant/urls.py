from django.conf.urls import include, url
from order.views import *

urlpatterns = [
    url(r'^manage_room',manage_room_views),
]
