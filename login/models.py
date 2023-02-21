
from django.db import models

# Create your models here.
class User(models.Model ):
        name=models.CharField(max_length=30,blank=True,null=True)
        number=models.CharField(max_length=30,blank=False,unique=True)   
        password=models.CharField(max_length=30,blank=True,null=True)
        

        def __str__(self):
            return self.number

