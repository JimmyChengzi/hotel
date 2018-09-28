from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^hotel/$",hotel_views),
    url(r"^test/$",test_views),
    url(r"page_2/",page2_views),
    url(r"page_3/",page3_views)
]