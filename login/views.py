from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView
from rest_framework.views import APIView
from .models import User
from django.shortcuts import redirect ,HttpResponse
from .serializer import UserSerializer
import socket





block_li=[]
def signup(request):
     firstname=request.POST.get("first_name","")
     lastname=request.POST.get("last_name","")
     password=request.POST.get("pass","")
     repeatpass=request.POST.get("reppass","")
     if firstname and lastname and password  and repeatpass  and password==repeatpass:
        User.objects.create(first_name=firstname,last_name=lastname,password=password,number=request.session['number'])
        return redirect("/login")
     else:
        return redirect("/signup")   
     return render(request,"login/signup.html")        
def checkcode(request):
        codes=[110,120,130,140,150,160,170,180]
        code1=request.POST.get("code","")   
        if int(code1)  in codes:
             return render(request,"login/signup.html")
        else :
                return render(request,"login/code.html")          
        return redirect("/checkcode" )  
# Create your views here.
def checknumber(request):
       
        number1=request.POST.get("number","")
        flag=User.objects.filter(number=number1).first()
        
        if flag is None:
                request.session['number']=number1
                print("no user")
                return render(request,"login/code.html")
        elif flag is not None :
                request.session['number']=str(flag.number)
                context={
                      "flag":flag  
                  }
                return render( request, "login/loginpass.html"   , context )
def number(request):
      
        return render(request,"login/login.html")
def checkpass(request):
          
          pass1=request.POST.get("pass","")
          flag=User.objects.filter(password=pass1).first()
          
          hostname=socket.gethostname()
          ip_address=socket.gethostbyname(hostname)
          if ip_address not in block_li:
                try:
                        request.session['counter']      
                except:
                        counter=0
                else:
                        counter=request.session['counter']
                
                                
                try:
                        request.session['username']   
                except:
                        request.session['username']=request.session['number'] 
                else:
                        if  request.session['username']!= request.session['number'] :      
                                counter=0
                
                        

                if flag is None:
                        counter=counter+1
                        request.session['counter']=counter
                        if counter >2:
                                block_li.append(ip_address)
                                
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

