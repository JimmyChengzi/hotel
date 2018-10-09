from django.db import models

# Create your models here.
Examine = (
    (0,'审核中'),
    (1,'审核通过'),
    (2,'审核失败')
)
class RoomType(models.Model):
    merchantId = models.CharField(max_length=30,verbose_name="商家id")
    title = models.CharField(max_length=30,verbose_name="房间名",null=False)
    picture = models.ImageField(upload_to="static/image/roomtype",null=True,verbose_name="房间图片")
    acreage = models.DecimalField(max_digits=7,decimal_places=2,verbose_name="建筑面积",null=False)
    floor = models.IntegerField(verbose_name="楼层",null=False)
    Bedtype = models.CharField(max_length=30,verbose_name="床型")
    window = models.CharField(max_length=30,verbose_name="窗户")
    price = models.IntegerField(verbose_name="价格")
    facility = models.CharField(max_length=30,verbose_name="配套设施")
    examine = models.IntegerField(choices=Examine,verbose_name="审核状态")
    stock = models.IntegerField(verbose_name="库存",default=1)
    isActive = models.BooleanField(verbose_name="是否激活")
    isShow = models.BooleanField(verbose_name="是否上架",default=True)
