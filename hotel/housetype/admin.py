from django.contrib import admin
from .models import *
# Register your models here.

# 定义在列表页展示的信息
class HotelAdmin(admin.ModelAdmin):
    list_display = ("title","id")
    ordering = ("-id",)  #"-id" 的话则倒序排序


admin.site.register(Hotel,HotelAdmin)
admin.site.register(room_message)