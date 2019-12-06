from django.urls import path

from . import views

urlpatterns = [
    path('', views.display),
    path('stats/', views.stats),
    path('map/', views.map),
    ]
