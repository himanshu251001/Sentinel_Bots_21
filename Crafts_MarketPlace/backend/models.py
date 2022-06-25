from django.db import models
#Create your models here.

class SellerData(models.Model):
    # unique_id = models.CharField(max_length=20, editable=False, unique=True,default="")
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    email_id = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10, unique=True,null=False,blank=False,default=0)
    username = models.CharField(max_length=20,unique=True, default='')
    password = models.CharField(max_length=20,default="")

class CustomerData(models.Model):
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    email_id = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10,unique=True,null=False,blank=False,default=0)
    username = models.CharField(max_length=20,unique=True, default='')
    password = models.CharField(max_length=20,default="")

class ProductsData(models.Model):
    name = models.CharField(max_length=50, default="")
    seller_id = models.ForeignKey(SellerData, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isAvailable = models.BooleanField(null=False, default=False)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    state = models.CharField(max_length=15,default="")
    
