
from django import views
from django.urls import path , include
from .views import home

#app_name = "agence"
    
    
urlpatterns = [
    path("home/", home , name="home"),
]


