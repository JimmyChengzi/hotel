from django.shortcuts import render
from merchant.urls import *
from merchant.models import *
from hotel.settings import MEDIA_ROOT
import os
from django.http import HttpResponse
# Create your views here.
def manage_room_views(request):
    if request.method == "GET":
        merchant_id = "11"
        AllRoom = RoomType.objects.filter(merchantId=merchant_id,isActive=True,isShow=True)
        return render(request,'room_manage.html',locals())

def change_room_views(request,roomtitle):
    if request.method == "GET":
        merchant_id = "11"
        title = roomtitle
        Room = RoomType.objects.get(merchantId=merchant_id,title = title,isActive=True, isShow=True)
        return render(request,'room_change.html',locals())
    elif request.method == 'POST':
        merchant_id = "11"
        title = request.POST.get('title')
        if title != roomtitle:
            TheRoom = RoomType.objects.filter(merchantId=merchant_id,title = title)
            if TheRoom:
                return HttpResponse('该类型房间名称已被使用')
            else:
                TheRoom = RoomType()
        else:
            TheRoom = RoomType.objects.get(merchantId=merchant_id, title=title)
        TheRoom.title = title
        filename = merchant_id + '_' + title + '.jpg'
        path = os.path.join(MEDIA_ROOT, filename)
        f1 = request.FILES.get('picture')
        print(f1)
        with open(path, 'wb') as pic:
            for p in f1.chunks():
                pic.write(p)
        TheRoom.picture = path
        TheRoom.save()
        return HttpResponse('修改成功')