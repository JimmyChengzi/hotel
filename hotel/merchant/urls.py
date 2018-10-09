from django.conf.urls import include, url
from merchant.views import *

urlpatterns = [
    url(r'^manage_room/$',manage_room_views),
    url(r'^change_room/([\s\S]*?)/',change_room_views,name='changeroom'),
]
