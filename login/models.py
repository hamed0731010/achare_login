from wsgiref.validate import validator
from django.db import models
from phonenumber_field import modelfields
import re

# Create your models here.
class User(models.Model ):
        id=models.AutoField(primary_key=True)
        first_name=models.CharField(max_length=15,blank=False)
        last_name=models.CharField(max_length=15,blank=False)  
        number=modelfields.PhoneNumberField(blank=False,unique=True )
        password=models.CharField(max_length=20,blank=False)


        def __str__(self):
            return self.first_name +" " +self.last_name

