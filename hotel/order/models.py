from django.db import models

# Create your models here.

class MerchantOrder(models.Model):
    merchantId = models.CharField(max_length=20,verbose_name="商家id",default=None,null=False)
    orderid = models.CharField(max_length=50,verbose_name="订单号")
    ordermessage = models.CharField(max_length=300,verbose_name="订单信息")
    def __str__(self):
        return self.orderid