from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import theProfiles, theProjects
from .serializer import MerchSerializer

# Create your views here.
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = theProjects.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = theProfiles.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

