from django.contrib import admin

from .models import  CustomerHistory, ProductPurchaseHistory, ProductsData, SellerData ,CustomerData

# Register your models here.
# class SellersDetails(admin.ModelAdmin):
#     list = ('id','unique_id','name','email_id')
# class CostumersData(admin.ModelAdmin):
    
admin.site.register(SellerData)
admin.site.register(CustomerData)
admin.site.register(ProductsData)
admin.site.register(ProductPurchaseHistory)
admin.site.register(CustomerHistory)