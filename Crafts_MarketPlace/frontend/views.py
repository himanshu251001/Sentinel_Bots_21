from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import  redirect, render, HttpResponse
from backend.models import CustomerData, SellerData
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def loginCustomer(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['Details']
        password = request.POST['Password_Details']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse('Success')
        else:
            return render(request,'errors/login_failed.html')
    else:   
        return render(request, 'registration/loginCustomer.html')

@csrf_exempt
def registerSeller(request, *args, **kwargs):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['Mail_id']
        fname=request.POST['First_Name']
        lname=request.POST['Last_Name']
        phone=request.POST['Contact_NO']
        pass1=request.POST['password_']
        pass2=request.POST['password__']
        pan = request.POST['PanCard']
        gstin = request.POST['GSTNumber']
        # check for errorneous input
        if len(username)<10:
            return HttpResponse("Minimum length required is 10")

        if not username.isalnum():
            return HttpResponse("Required AlphaNumeric")
        if (pass1!= pass2):
            return HttpResponse("Password doesnt match")
        
        # Create the user
        if(User.objects.filter(username=username).count() == 0 & User.objects.filter(email=email).count()==0):
            try:
                myuser = User.objects.create_user(username, email, pass1)
                newData = SellerData.objects.create(fname=fname,lname=lname,phone=phone,credentials=myuser,PAN=pan,GSTIN=gstin)
                newData.save()
                myuser.first_name= fname
                myuser.last_name= lname
                myuser.save()
                return render(request,'errors/success.html')
            except:
                User.objects.filter(username=username).delete()
                return render(request,'errors/existErrorSeller.html')
        else:
            return render(request,'errors/existErrorSeller.html')

        # messages.success(request, " Your iCoder has been successfully created")

    else:
        return render(request,'registration/registerSeller.html')
@csrf_exempt
def registerCustomer(request,*args,**kwargs):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['mail']
        fname=request.POST['FirstName']
        lname=request.POST['lastName']
        phone=request.POST['phone']
        pass1=request.POST['password']
        pass2=request.POST['password_conf']

        if len(username)<10:
            return HttpResponse("Minimum length required is 10")

        if not username.isalnum():
            return HttpResponse("Required AlphaNumeric")
        if (pass1!= pass2):
            return HttpResponse("Password doesnt match")
        if(User.objects.filter(username=username).count() == 0 & User.objects.filter(email=email).count()==0):
            try:
                myuser = User.objects.create_user(username, email, pass1)
                newData = CustomerData.objects.create(credentials=myuser,fname=fname,lname=lname,phone=phone)
                newData.save()
                myuser.first_name= fname
                myuser.last_name= lname
                myuser.save()
                return render(request,'errors/success.html')
            except:
                User.objects.filter(username=username).delete()
                return render(request,'errors/existError.html')

        else:
            return render(request,'errors/existError.html')
    else:
        return render(request,'registration/registerCustomer.html')


def Clothing_Page(request):
    return render(request,'products/Clothing_Page.html')
def Fashion_Accessories(request):
    return render(request,'products/Fashion_Accessories.html')
def Stone_Works(request):
    return render(request,'products/Stone_works.html')
def Traditional_Wears(request):
    return render(request,'products/Traditional_Wear.html')
def Wood_Words(request):
    return render(request,'products/Wood_Works.html')
def home(request):
    return render(request,'home.html')
def analyze(request):
    return render(request,'analyze.html')