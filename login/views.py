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

#password hash shode nist ,dade ha validate nashodan , modiriate khata  ,ekhtarha and meeages
blocked_ip={}
#for sign up
def signup(
        request):
     firstname=request.POST.get("first_name","")
     lastname=request.POST.get("last_name","")
     password=request.POST.get("pass","")
     repeatpass=request.POST.get("reppass","")
     if firstname and lastname and password  and repeatpass  and password==repeatpass:
        User.objects.create(first_name=firstname,last_name=lastname,password=password,number=request.session['number'])
        return redirect("/login")
     else:
        return render(request,"login/signup.html")   
     return render(request,"login/signup.html")        
#for checking the authontication code     
def checkcode(
           request):
        code=int(random.randrange(100000,999999))   
        messages.info(request,f"your code is {code}")
        code1=request.POST.get("code","")   
        if int(code1) == code:
             return render(request,"login/signup.html")
        else :
                return render(request,"login/code.html")          
        return redirect("/checkcode" )  
# for checking the phone number
def checknumber(
             request):
       
        number1=request.POST.get("number","")
        flag=User.objects.filter(number=number1).first()
        
        if flag is None:
                request.session['number']=str(number1)
                print("no user")
                return render(request,"login/code.html")
        elif flag is not None :
                request.session['number']=str(flag.number)
                context={
                      "flag":flag  
                  }
                return render( request, "login/loginpass.html"   , context )
#first login form base phone number                
def number(
           request):
      
        return render(request,"login/login.html")
#for checking the pass        
def checkpass(
             request):
          
          pass1=request.POST.get("pass","")
          flag=User.objects.filter(password=pass1).first()
          
          hostname=socket.gethostname()
          ip_address=socket.gethostbyname(hostname)
          if (ip_address not in blocked_ip.keys()) or (blocked_ip[ip_address]+ datetime.timedelta(minutes=60)<datetime.datetime.now()):
                try:
                        request.session['counter']      
                except:
                        counter=0
                else:
                        counter=request.session['counter']
                
                                
                try:
                        request.session['user']   
                except:
                        request.session['user']=request.session['number'] 
                else:   
                        a=request.session['user']
                        b=request.session['number']
                        if  a != b :      
                                counter=0
                
                        

                if flag is None:
                        counter=counter+1
                        request.session['counter']=counter
                        if counter >2:
                                #block_li.append(ip_address)
                                t=datetime.datetime.now()
                                blocked_ip[ip_address]=t
                                return HttpResponse(f"{ip_address} you are blocked for 1 hours")
                        
                        return render(request,"login/loginpass.html") 
                elif flag is not None:      
                        return HttpResponse(f"you are login with {flag.first_name } ")
          elif ip_address in block_li:
                 return HttpResponse(f"{ip_address} you are blocked for 1 hours")

          return redirect( "/checkpass" ) 
class UserList(ListAPIView):
        queryset=User.objects.all()
        serializer_class=UserSerializer
        
class RetrieveUser(ListCreateAPIView):
        queryset=User.objects.all()
        serializer_class=UserSerializer
class Check(APIView):
       
        def check_phone(
                   self,request):
              number=request.data['number']
              flag=User.objects.filter(number=number)
              
              if flag is None:

                 print("no user")
                 return redirect('/user')
              elif flag is not None :
                  
                  
                  return HttpResponse("you have account")
              return Response({"data":"done"})

