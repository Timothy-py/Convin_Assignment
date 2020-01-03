from django.urls import path
from . import views

app_name = 'system1'

urlpatterns = [
    path('home', views.home)
]