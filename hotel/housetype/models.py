from django.db import models

"""
superuser:root
password:123456...
"""

# Create your models here.
ROOMTYPE = (
    (0,"经济房"),
    (1,"一房一厅"),
    (2,"两房一厅"),
    (3,"无房")
)

class Hotel(models.Model):
    hotel_user = models.CharField("酒店账户",max_length=30,null=False)
    hotel_pwd = models.CharField("密码",max_length=100,null=False)

    title = models.CharField("酒店名",max_length=20,null=False)
    address = models.CharField("地址",max_length=100,null=False)
    pic = models.ImageField("展示图",upload_to="static/housetype/img/",default='static/housetype/img/defa.jpg')
    isActive = models.BooleanField("是否激活",default=True,null=False)

    def __str__(self):
        return self.title

class room_message(models.Model):
    hotel_id = models.ForeignKey(Hotel)
    # 房间种类
    room_type = models.IntegerField("房间类型",choices=ROOMTYPE,null=False)
    # 房间面积
    room_sq = models.IntegerField("房间面积",null=False )
    # 是否有窗
    room_window = models.BooleanField("是否有窗",default=True,null=False)
    # 窗户图片
    room_pic1 = models.ImageField("图片1",upload_to="static/housetype/img/room",null=False)
    room_pic2 = models.ImageField("图片2", upload_to="static/housetype/img/room/", null=False)
    room_pic3 = models.ImageField("图片3", upload_to="static/housetype/img/room/", null=False)
    room_pic4 = models.ImageField("图片4", upload_to="static/housetype/img/room/", null=False)
    isActive = models.BooleanField("是否激活",default=True,null=False)
    def __str__(self):
        return self.room_type

# 评价表 于用户表 和 房间表联系  //
#class

