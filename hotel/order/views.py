from django.shortcuts import render
from django.core import serializers
from order.models import *
from django.http import HttpResponse
import json

# Create your views here.
def login_merchant(func):
    def login_func(request,*args,**kwargs):
        if request.session.get('merchant_id',None):
            return func(request,*args,**kwargs)
        else:
            response = redirect('/merchant_login')
            response.set_cookie('url',request.url)
def merchant_order_views(requst):
    if requst.method == 'GET':
        # merchant_id = request.session.get('merchantId')
        merchant_id = '11'

        orderlist = MerchantOrder.objects.filter(merchantId=merchant_id)
        print(orderlist)
        pagecount = orderlist.count()//5
        if orderlist.count()%5 != 0:
            pagecount += 1
        showorders = orderlist[0:5]
        pagelist = []
        print(pagecount)
        for p in range(1,pagecount+1):
            print(p)
            pagelist.append(str(p))
        print(orderlist.count())
        # for order in showoders:
        #     print(order.ordermessage)
        return render(requst,'merchant_order.html',locals())

def merchant_order_pages_views(requst):
    page = int(requst.POST.get('page')[4::])
    print(page)
    merchant_id = "11"
    orderlist = MerchantOrder.objects.filter(merchantId=merchant_id)
    type(orderlist)
    start = (page-1)*5
    stop = start + 5
    showoders = orderlist[start:stop]
    pagecount = orderlist.count() // 5
    if orderlist.count() % 5 != 0:
        pagecount += 1
    pagelist = []
    print(pagecount)
    for p in range(1, pagecount + 1):
        print(p)
        pagelist.append(str(p))
    orderStr = serializers.serialize('json',showoders)
    pageStr = json.dumps(pagelist)
    dic = {"pagelist":pageStr,"showorders":orderStr}
    jsonStr = json.dumps(dic)
    print(jsonStr)
    return HttpResponse(jsonStr)