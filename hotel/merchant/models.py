from django.db import models

# Create your models here.
class RoomType(models.Model):
    merchantId = models.CharField(max_length=30,verbose_name="商家id")
    userId = models.CharField(max_length=30,verbose_name="用户id")
    title = models.CharField(max_length=30,verbose_name="房间名")
    picture = models.ImageField(upload_to="static/image/roomtype",null=True,verbose_name="房间图片")
    acreage = modles.DecimalField(max_digits=7,max_places=2,verbose_name="建筑面积")
    floor = models.InterField(verbose_name="楼层")
    Bedtype = models.CharField(max_length=30,verbose_name="床型")
    