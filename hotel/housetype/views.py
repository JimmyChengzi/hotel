from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json
import copy as c
# 将数据库的得到的列表分割为多个长度固定的列表 组成的列表    深度拷贝的理解应用
def cut_list(L,length):
    # 中间生成的length个元素组成的列表A
    page_list = []
    # 由每页的列表A组成的列表
    all_list = []
    bList = list(c.deepcopy(L))
    print(bList)
    for page in L:
        page_list.append(bList[0])
        #print(bList[0], end="\t")
        #print(L)
        del bList[0]

        if len(page_list) == length:
            print(page_list)
            all_list.append(page_list)
            page_list= []
            if len(bList) < length:
                all_list.append(bList[:])
                # print(bList)
                break

    #print(all_list)
    return all_list



# Create your views here.
def test_views(request):
    return HttpResponse("<h1>ok!!!</h1>")

def hotel_views(request):
    hotel = Hotel
    h_list = hotel.objects.filter()
    #print(h_list)
    page_list = cut_list(h_list,5)
    page_1 = page_list[0]
    length = list(range(1,len(page_list)+1))
    #print(page_list)
    return render(request,"hotel.html",locals())

def page2_views(request):
    return render(request,"test1.html")

def page3_views(request):
    return HttpResponse("<h1>测试page3</h1>")