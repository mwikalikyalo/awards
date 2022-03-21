from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import theProfiles, theProjects
from .serializer import MerchSerializer
from rest_framework import status
from .models import Profile,Project
from .forms import CreateUserForm,ProfileForm,ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    projects = Project.objects.all().order_by("published").reverse()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit = False)
            profile.user = Profile.objects.get(user_id = current_user.id)
            profile.save()
        return redirect("home") 
    else:
        form = ProjectForm()    
    return render(request, 'home.html', {'projects':projects, "current_user":current_user})


"""New profile page if you are a new user """
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user

    try:
        Profile.objects.get(user_id = current_user.id)
        return redirect("home")

    except:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit = False)
                profile.user = current_user
                profile.save()

            return redirect("home")   

        else:
            form = ProfileForm()

    return render(request, 'create_profile.html', {"form": form, "current_user":current_user}) 


"""View profile"""
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =  Profile.objects.filter(user = User(id = current_user.id)).first()
    projects = Project.objects.filter(profile = profile.pk ).all() 
        
    return render(request, 'profile.html', {"profile": profile, "projects":projects, "current_user": current_user})    


""" Uploading images"""
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = Profile.objects.get(user_id = current_user.id)
            project.save()
        return redirect("home")   

    else:
        form = ProjectForm()
    return render(request, 'post.html', {"form": form, "current_user":current_user}) 


class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = theProjects.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = theProfiles.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

