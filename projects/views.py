from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import theProfiles, theProjects
from .serializer import MerchSerializer
from rest_framework import status
from .models import Profile,Project
from .forms import CreateUserForm,ProfileForm,ProjectForm

# Create your views here.
def home(request):
    projects=Project.objects.all()

    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        projects=projects.filter(title__icontains=item_name)
    else:
        projects=Project.objects.all()

    return render(request,'home.html',{'projects':projects})


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
        return redirect('index')
    else:
        form=ProfileForm()

    return render(request,'create-profile.html',{"form":form})


def profile(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    projects=Project.objects.filter(user=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})
    

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

