from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print('===================DESDE LA APP DEPARTAMENTO============')

urlpatterns = [
    path('departamento/',DesdeApps),
]