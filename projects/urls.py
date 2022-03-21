from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/register/', views.register, name='register'),
  path('accounts/login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('create/profile/',views.create_profile, name='create_profile'),
  path('profiles/',views.profile, name='profile'),
  path('new/project/',views.new_project, name='new_project'),
  path('api/project/', views.ProjectList.as_view()),
  path('api/profile/', views.ProfileList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)