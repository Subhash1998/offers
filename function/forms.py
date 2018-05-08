from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Feature,UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('first_name','email','username','password')


class FeatureForm(forms.ModelForm):
	class Meta:
		model=Feature
		fields=('feature_name','feature_detail')

class CompanyForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('company',)