import datetime
from django.db import models
from django.contrib.auth.models import User
#Create your models here.

class SellerData(models.Model):
    # unique_id = models.CharField(max_length=20, editable=False, unique=True,default="")
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10, unique=True,null=False,blank=False,default=0)
    credentials = models.OneToOneField(User, on_delete=models.CASCADE)
    PAN = models.CharField(max_length=10,default="",unique=True)
    GSTIN = models.CharField(max_length=15,default='',unique=True)

class CustomerData(models.Model):
    credentials = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10,unique=True,null=False,blank=False,default=0)
    
class ProductsData(models.Model):
    name = models.CharField(max_length=50, default="")
    seller_id = models.ForeignKey(SellerData, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isAvailable = models.BooleanField(null=False, default=False)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    state = models.CharField(max_length=15,default="")

class ProductPurchaseHistory(models.Model):
    data = models.ForeignKey(ProductsData,on_delete=models.CASCADE)
    purchased_date = models.DateTimeField(editable=False)

    def save(self):
        self.purchased_date = datetime.date.today()
        super(ProductPurchaseHistory, self).save()

class CustomerHistory(models.Model):
    product_purchased = models.ManyToManyField(ProductPurchaseHistory,blank=True)
    # username = models.OneToOneField(CustomerData,on_delete=models.CASCADE,unique=True)
    username = models.CharField(default='',max_length=20)
    