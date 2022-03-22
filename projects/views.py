from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import theProfiles, theProjects
from django.urls import reverse
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework import status
from .models import Profile,Project,Ratings
from .forms import CreateUserForm,ProfileForm,ProjectForm,RatingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout as dj_login
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects=Project.objects.all()

    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        projects=projects.filter(title__icontains=item_name)
    else:
        projects=Project.objects.all()

    return render(request,'home.html',{'projects':projects})


def register(request):
    title = 'Register - AwardIT'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            'title':title,
            'form':form,
                        }
    return render(request, 'registration/registration_form.html', context)


def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)


def logout(request):  

    return redirect(reverse('login'))


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if request.current_user.is_authenticated:
            form.instance.user = request.user
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user

            profile.save()
        return redirect('home')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    projects=Project.objects.filter(user=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
  
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            # project.avatar = profile.avatar
            project.save()
    else:
        form = ProjectForm()

    return render(request,'post.html',{"form":form})


# @login_required(login_url='/accounts/login/')
# def ratings(request, id):
#     current_user = request.user
#     project = Project.objects.filter(pk = id).first()
#     ratings = Ratings.objects.filter(project = project, user = current_user)
    
#     if request.method == 'POST':
#         if ratings:
#             messages.error(request, 'You have already rated this project')
#             raise PermissionDenied('You have rated this project.')        
#         else:
#             form = RatingForm(request.POST, request.FILES)
#             if form.is_valid():
#                 rating = form.save(commit = False)
#                 design = form.cleaned_data['design']
#                 usability = form.cleaned_data['usability']
#                 content = form.cleaned_data['content']
#                 rating.user = current_user
#                 rating.project = project
#                 rating.average = (float(design) + float(usability) + float(content)) /3
#                 rating.save()

#             return redirect("home")   

#     else:
#         form = RatingForm()  

    # return render(request, 'ratings.html', {"current_user":current_user , "form":form, "project":project}) 


class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = theProjects.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = theProfiles.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

