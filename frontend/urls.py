from django.urls import path
from .views import  Clothing_Page, Fashion_Accessories, Stone_Works, Traditional_Wears, Wood_Words, analyze, home, loginCustomer, registerCustomer, registerSeller
urlpatterns = [
    path('',home),
    path('loginCustomer/',loginCustomer),
    path('registerSeller/',registerSeller),
    path('registerCustomer/',registerCustomer),
    path('Clothing_Page/',Clothing_Page),
    path('Stone_Works/',Stone_Works),
    path('Fashion_Accessories/',Fashion_Accessories),
    path('Traditional_Wear/',Traditional_Wears),
    path('Wood_Works/',Wood_Words),
    path('analyze/',analyze)
]