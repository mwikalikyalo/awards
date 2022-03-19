from django.contrib import admin
from .models import Profile, Project
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(User)