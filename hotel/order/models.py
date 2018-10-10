from django.db import models

# Create your models here.

OrderStatus = (
    (1,"已支付未入住"),
    (2,"入住中"),
    (3,"已过期"),
    (0,"已取消")
)
class MerchantOrder(models.Model):
    merchantId = models.CharField(max_length=20,verbose_name="商家id",default=None,null=False)
    roomtype = models.CharField(max_length=20,verbose_name="房间类型",default="无")
    orderid = models.CharField(max_length=50,verbose_name="订单号")
    ordermessage = models.CharField(max_length=300,verbose_name="订单信息")
    orderstatus = models.IntegerField(choices=OrderStatus,verbose_name="订单状态",default=1)
    number = models.IntegerField(verbose_name="预订房间数",default=1)
    def __str__(self):
        return self.orderid