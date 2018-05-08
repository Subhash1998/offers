from rest_framework import models
from rest_framework import serializers
from .models import UserProfile,Feature
from django.contrib.auth.models import User

class StockSerializer1(serializers.ModelSerializer):

      class Meta:
            model = User
            #fields = ('ticker','volume')
            fields = ('first_name','email','username','password')


class StockSerializer2(serializers.ModelSerializer):

      class Meta:
            model = UserProfile
            fields = '__all__' 


class StockSerializer3(serializers.ModelSerializer):

      class Meta:
            model = Feature
            #fields = ('ticker','volume')
            fields = '__all__' 
