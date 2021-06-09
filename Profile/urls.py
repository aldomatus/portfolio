#   Django 
from django.urls import path

#   Views
from Profile import views

urlpatterns = [

    path('', views.feed_view, name='feed')
    
]