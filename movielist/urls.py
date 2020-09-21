from django.urls import path
from movielist import views

urlpatterns = [
    path('', views.index, name="home"),
]
