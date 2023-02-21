# from django.core.validators import MinLengthValidator,RegexValidator
# from django.db import models
# import re
# from django import forms
# from .models import User

# class UserForm(forms.ModelForm ):
#         name=forms.CharField(max_length=15,blank=True)  
#         phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the correct format ")
#         number = forms.CharField(validators=[phone_regex], max_length=11,validators=[MinLengthValidator(11)]) # validators should be a list
#         password=forms.CharField(widget=forms.PasswordInput,blank=False)
#         class Meta:
#                 model = User