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

# 改变房型信息页面
def change_room_views(request,roomtitle):
    if request.method == "GET":
        merchant_id = "11"
        title = roomtitle
        try:
            Room = RoomType.objects.get(merchantId=merchant_id,title = title,isActive=True, isShow=True)
        except:
            return HttpResponse('数据不存在或已更新')
        return render(request,'room_change.html',locals())
    elif request.method == 'POST':
        merchant_id = "11"
        title = request.POST.get('title')
        TheRoom = RoomType.objects.get(merchantId=merchant_id, title=roomtitle)
        if title != roomtitle:
            CheackRoom = RoomType.objects.filter(merchantId=merchant_id,title = title)
            if CheackRoom:
                return HttpResponse('该类型房间名称已被使用')
            else:
                TheRoom.title = title
        filename = merchant_id + '_' + str(TheRoom.id) + '.jpg'
        path = os.path.join(MEDIA_ROOT, filename)
        f1 = request.FILES.get('picture')
        if f1:
            with open(path, 'wb') as pic:
                for p in f1.chunks():
                    pic.write(p)
            TheRoom.picture = '/static/image/roomtype/' + filename
        TheRoom.save()
        return HttpResponse('修改成功')

# 增加房型页面
def add_newroom_views(request):
    if request.method == "GET":
        return render(request,'room_add.html')
    elif request.method == 'POST':
        merchant_id = "11"
        title = request.POST.get('title')
        CheackRoom = RoomType.objects.filter(merchantId=merchant_id,title = title)
        if CheackRoom:
            return HttpResponse('该类型房间名称已被使用')
        TheRoom = RoomType()
        TheRoom.title = title
        filename = merchant_id + '_' + str(TheRoom.id) + '.jpg'
        path = os.path.join(MEDIA_ROOT, filename)
        f1 = request.FILES.get('picture')
        if f1:
            with open(path, 'wb') as pic:
                for p in f1.chunks():
                    pic.write(p)
            TheRoom.picture = '/static/image/roomtype/' + filename
        TheRoom.merchantId = merchant_id
        TheRoom.acreage = 11.11
        TheRoom.floor = 5
        TheRoom.price = 600
        TheRoom.examine = 1
        TheRoom.isActive = True
        TheRoom.save()
        return HttpResponse('修改成功')