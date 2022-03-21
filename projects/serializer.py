from rest_framework import serializers
from .models import theProfiles, theProjects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = theProjects
        fields = ('title', 'about')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = theProfiles
        fields = ('user', 'bio', 'email')