from .views import UserList,RetrieveUser
from django.urls import path,include
from . import views

app_name='login'

urlpatterns=[
   path("",UserList.as_view()   ,name='user'),
     path("user",RetrieveUser.as_view()   ,name='username'),
      path("login",views.number   ,name='login'),
       path('checknumber',views.checknumber  , name= 'checknumber'),
        path('checkpass',views.checkpass  , name= 'checkpass'),
        path('checkcode',views.checkcode  , name= 'checkcode'),
         path('signup',views.signup  , name= 'signup'),
]


