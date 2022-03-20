from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import theProfiles, theProjects
from .serializer import MerchSerializer
from rest_framework import status

# Create your views here.


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

