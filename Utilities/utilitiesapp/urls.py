from django.contrib import admin
from django.urls import path, include
from utilitiesapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('', views.home),
   path('createservice', views.create_service),
   path('showservice', views.show_services),
   path('register', views.register),
   path('login', views.user_login),
   path('logout', views.user_logout),
   path('edit/<rid>', views.edit_service)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
