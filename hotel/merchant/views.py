from django.shortcuts import render
from merchant.urls import *
# Create your views here.
def manage_room_views(request):
    if request.method == "GET":
        merchant_id = "11"
