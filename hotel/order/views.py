from django.shortcuts import render

# Create your views here.
def login_merchant(func):
    def login_func(request,*args,**kwargs):
        if request.session.get('merchant_id',None):
            return func(request,*args,**kwargs)
        else:
            response = redirect('/merchant_login')
            response.set_cookie('url',request.url)
def merchant_order(requst):
    merchant_id = request.session.get('merchant_id')
    orderlist = Order.objects.filter(merchant_id=merchant_id).order_by("time")
    ordercount = orderlist.count()
    return render(requst,'merchant_order.html',locals())
