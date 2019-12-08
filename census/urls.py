from django.urls import path

from . import views

urlpatterns = [
    path('', views.display),
    path('stats/', views.stats),
    path('<str:squirrel_id>/',views.edit),
    path('add/',views.add),
    ]
