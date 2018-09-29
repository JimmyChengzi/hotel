from django.shortcuts import render
import json
from order.models import *
from django.http import HttpResponse

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
        pagecount = orderlist.count()//5+1
        showorders = orderlist[0:5]
        print(showorders)
        pagelist = []
        for p in range(pagecount):
            pagelist.append(p)
        print(orderlist.count())
        # for order in showoders:
        #     print(order.ordermessage)
        return render(requst,'merchant_order.html',locals())

def merchant_order_pages_views(requst):
    page = int(requst.POST.get('page')[4::])
    orderlist = MerchantOrder.objects.filter(merchant_id=merchant_id).order_by("time")
    ordercount = orderlist.count()
    start = (page-1)*5
    stop = start + 5
    showoders = orderlist[start:stop]
    jsonStr = json.dumps(showoders)
    return HttpResponse(jsonStr)