from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('doctorlist.html/index.html/', views.index),
    path('doctorlist.html/', views.doctors),
    path('index.html/doctorlist.html', views.doctors),
]
