from django import forms
from .models import Neighborhood,Profile,Business,Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude = ['owner']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude =['occupant']

