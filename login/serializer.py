from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields="__all__"

