from random import random
from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView
from rest_framework.views import APIView
from .models import User
from django.shortcuts import redirect ,HttpResponse
from .serializer import UserSerializer
import socket
import datetime
from django.contrib import messages
import random
from ippanel import Client
from django.db.models import Q
# you api key that generated from panel


...


#signup
def signup(request):
     if request.method=="POST":
        phone=request.POST.get("phone")
        password=request.POST.get("pass")
     
        if password !=None and phone !=None:
                try:
                        User.objects.create(number=phone,password=password)
                        return redirect("/login")
                except:
                      messages.error("phone number is invalid or Repetitious") 
     return render(request,"login/signup.html")        
#for checking the user login     
def login(request):
        if request.method=="POST":
                phone=request.POST.get("phone")
                password=request.POST.get("pass")
                auth_user=User.POST.get(Q(number=phone) & Q(password=password))
                if auth_user:
                         return HttpResponse("you logged in succesfully")
                else:
                     return redirect("/login")
        return render(request,"login/login.html")  



# for checking the code
def otp(request):
        
        if request.method=="POST":
                api_key = "Fs2SgWGY9SmClVJUBlOiCxyjAD7LCLsQBlnl-oSyp4U="
# create client instance
                sms = Client(api_key)
# return float64 type credit amount
                #credit = sms.get_credit()
                phone=request.POST.get("phone")
                if phone:
                        request.session['code']=int(random.randrange(100000,999999))  
                        code=request.session['code']
                        user,  created=User.objects.get_or_create(number=phone)
                        
                        if user:
                                
                                message_id = sms.send(
                                                "+9890000145",          # originator
                                                [f'{user.number}'],    # recipients
                                                "this is your code:  f'{code}'  ",# message
                                                "description"        # is logged
                                                )
                                return redirect("/check") 
                        else:
                               messages.error('incorrect')
        return render(request,"login/otp.html")  


#check code
def check_code(request):
       if request.method=="POST":
                code=request.POST.get("code")
                if code and request.session['code']==code :
                        return HttpResponse("successfully import")
                else:
                       return render(request,"login/check.html") 
       return render(request,"login/check.html")                  
