from django.contrib import admin
from django.urls import path,include
from dbapp import views

urlpatterns = [
    path('',views.index),
    path('insert/',views.insert),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]
