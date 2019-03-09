from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("registr/", views.registr, name="registr"),
    path('reset/', views.reset, name='reset'),
    path('example/', views.example, name='example'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('advertice/', views.advertice, name='advertice'),
    path("developer/", views.developer, name='developer'),
    path('recover/', views.recover, name='recover')
]