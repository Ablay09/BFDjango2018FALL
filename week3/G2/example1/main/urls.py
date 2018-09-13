from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('about/', views.about)
]
