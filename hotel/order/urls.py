from django.conf.urls import include, url
from order.views import *

urlpatterns = [
    url(r'^merchant_order/$',merchant_order_views),
    url(r'^m_o_pages/$',merchant_order_pages_views),
]
