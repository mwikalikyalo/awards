import email
from django.test import TestCase
from .models import Profile, Project 
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'mwikali')
        self.user.save()
        self.mwikali = Profile(user = self.user, id = self.user.profile.id, bio = 'You are doing great.', profile_photo = 'default.png', email= 'winniemwikali07@gmail.com')
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()        

    def test_instance(self):
        self.assertTrue(isinstance(self.mwikali, Profile))

    def test_saveProfile(self):
        self.mwikali.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)


class ProjectTestClass(TestCase):
    def setUp(self):
        self.user=User(username='chichi')
        self.user.save()
        self.project=Project(image='default.png',title = 'photo-django',description='This is a Django gallery project which shows different images of different locations and categories.',profile=self.user.profile, project_url = 'https://photo-00001.herokuapp.com/')   

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_saveProject(self):
        self.project.save_project()
        project_saved = Project.objects.all()
        self.assertTrue(len(project_saved) > 0)