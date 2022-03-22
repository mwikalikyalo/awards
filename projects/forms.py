from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Profile, Ratings

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model =  Project
        exclude = [ 'design']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_photo', 'email']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['project', 'user', 'average']