from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]