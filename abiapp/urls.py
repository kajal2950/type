from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.index, name='index'),
    path('category/<str:slug>', views.category, name="category"),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('blog',views.blog, name='blog'),
    path('videos',views.videos, name='videos'),
  
    
    
]

