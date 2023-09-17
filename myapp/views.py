import random
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
from seller.models import *



# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method =="POST":
        try:
            user_data = User.objects.get( email=request.POST['email'])
            return render(request,'register.html',{'msg':'User already Exist'})
        except:
        
            if request.POST['pwd'] == request.POST['cpwd']:
                global fotp
                fotp = random.randint(1000,9999)
                subject = 'Your OTP Verfication'
                message = f"Hi your OTP is {fotp}, thank you for registering in 369 Mayurs Coffee"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                # User.objects.create(
                temp= {
                "name":request.POST["name"],
                "email":request.POST["email"],
                "mob":request.POST["mob"],
                "password":request.POST["pwd"]
                }
                return render(request,'otp.html')
            
            else:
                return render(request,'register.html',{'msg':'password and confirm password not match'})
    else:    
        return render(request,'register.html')
    
def otp(request):
    if request.method=="POST":
        if fotp == int(request.POST['otp']):
            User.objects.create(
                name=temp["name"],
                email=temp["email"],
                mob=temp["mob"],
                password=make_password(temp["password"])
            )
            return render(request,'register.html',{'msg':'Regestration Successfully'})
        else:
            return render(request,'otp.html',{'msg':'OTP not match'})
    else :

        return render(request,'register.html')

def login(request):
    if request.method == "POST":
     try:
        user_data = User.objects.get( email = request.POST["email"])
        #if user_data.password == request.POST["pwd"]:
        if check_password(request.POST['pwd'],user_data.password):
            request.session["email"]=request.POST["email"]
            session_data = User.objects.get( email = request.session["email"])
            return render(request,'index.html',{"session_data":session_data})
        else:
            
            return render(request,'login.html',{'msg':'password not match'})
     except:
            return render(request,'login.html',{'msg':'user not exist'})
    else:
            return render(request,'login.html')

def logout(request):
    del request.session["email"]
    return render(request,'login.html',{'msg':'logout successfully'})

def profile(request):
    if request.method == "POST":
        session_data = User.objects.get( email = request.session["email"])
        try:
            image_data=request.FILES["img"]
        except:
            image_data=session_data.propic

        if request.POST['opwd'] and request.POST['npwd'] and request.POST['cnpwd']:

            if check_password(request.POST['opwd'],session_data.password):

                if request.POST['npwd'] and request.POST['cnpwd']:
                    
                 

                    session_data.name=request.POST["name"]
                    session_data.mob=request.POST["mob"]
                    session_data.password=make_password(request.POST["npwd"])
                    session_data.propic=image_data
                    session_data.save()
                    return render(request,'profile.html',{"session_data":session_data, "msg":'Updated successfully'})

                 
                else:
                    return render(request,'profile.html',{"session_data":session_data, "msg":'New password and confirm new password not match'})

            else:
                return render(request,'profile.html',{"session_data":session_data, "msg":'old password not match'})

            
        else:
            session_data.name=request.POST["name"]
            session_data.mob=request.POST["mob"]
            session_data.propic=image_data
            session_data.save()
        return render(request,'profile.html',{"session_data":session_data, "msg":'Updated successfully'})
    else:
        session_data = User.objects.get( email = request.session["email"])
        
        return render(request,'profile.html',{"session_data":session_data})
    
def service(request):
    session_data = User.objects.get( email = request.session["email"])
    if request.method=="POST":
        return render(request,'service.html',{"session_data":session_data})
    else:
        return render(request,'service.html',{"session_data":session_data})

def booktable(request):
    if request.method=="POST":
        session_data = User.objects.get( email = request.session["email"])

        return render(request,'booktable.html',{"session_data":session_data})
    else:
        session_data = User.objects.get( email = request.session["email"])

        table_number=random.randint(1,50)
        return render(request,'booktable.html',{"table_number":table_number})

def cust(request):
    if request.method=="POST":
        session_data = User.objects.get( email = request.session["email"])
       
        return render(request,'cust.html',{"session_data":session_data})
    else:
        session_data = User.objects.get( email = request.session["email"])

        return render(request,'cust.html',{"session_data":session_data})
def about(request):
    session_data=User.objects.get(email = request.session["email"])
    return render(request,'about.html',{"session_data":session_data})
   

        



