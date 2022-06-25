from django.contrib.auth.models import User

from django.shortcuts import  redirect, render, HttpResponse
# from django.template import RequestContext
from backend.models import SellerData

# Create your views here.

def registerSeller(request, *args, **kwargs):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        # check for errorneous input
        if len(username)<10:
            return HttpResponse("Minimum length required is 10")

        if not username.isalnum():
            return HttpResponse("Required AlphaNumeric")
        if (pass1!= pass2):
            return HttpResponse("Password doesnt match")
        
        # Create the user
        if(User.objects.filter(username=username).count() == 0 & User.objects.filter(email=email).count()==0):
            myuser = User.objects.create_user(username, email, pass1)
            newData = SellerData.objects.create(fname=fname,lname=lname,email_id=email,phone=phone,username=username,password=pass1)
            newData.save()
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("Failed")

        # messages.success(request, " Your iCoder has been successfully created")

    else:
        return render(request,'registration/register.html')
