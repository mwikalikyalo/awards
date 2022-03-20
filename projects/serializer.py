from rest_framework import serializers
from .models import theProfiles, theProjects

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = theProjects
        fields = ('title', 'about')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = theProfiles
        fields = ('user', 'bio', 'email')