
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test ),
    path('notes/', views.getNotes ),
    path('notes/<str:pk>/', views.getNote ),

]
