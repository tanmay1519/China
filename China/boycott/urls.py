from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home" ),
    path('AtmaNirbhar/',views.Atma,name="atma" ),
    path('check/',views.result,name="result" ),
    path('add/',views.add,name="add" ),
]
