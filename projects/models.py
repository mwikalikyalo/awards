from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank = True, null=True)
    profile_photo = models.ImageField(upload_to = 'profile/', blank = True, null=True)
    email = models.CharField(max_length = 40, blank = True, null=True)

    def save_profile(self):
        self.save() 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
      if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Project(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField('image')
    about = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_url = models.URLField()
    published = models.DateField(auto_now_add=True)

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
    def save_project(self):
        self.save()   

class Ratings(models.Model):
    design = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    usability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    content = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    average = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default = 0.0) 

class theProfiles(models.Model):
    user = models.CharField(max_length=40)
    bio = models.TextField()
    email = models.EmailField()

class theProjects(models.Model):
    title = models.CharField(max_length=40)
    about = models.TextField()


