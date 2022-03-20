from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('create/profile/',views.create_profile, name='create_profile'),
  path('profiles/',views.profile, name='profile'),
  path('api/merch/', views.MerchList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)