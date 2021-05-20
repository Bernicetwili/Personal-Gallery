from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'photos'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    #path('add/', views.addPhoto, name='add'),
]+ static(
  settings.MEDIA_URL, 
  document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
