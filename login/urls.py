
from django.urls import path,include
from . import views

app_name='login'

urlpatterns=[

      path("login",views.login   ,name='login'),
      path('check',views.check_code  , name= 'check'),
      path('otp',views.otp  , name= 'otp'),
      path('signup',views.signup  , name= 'signup'),
]


