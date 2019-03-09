from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("registr/", views.registr, name="registr"),
    path('reset/', views.reset, name='reset'),
    path('example/', views.example, name='example'),
]