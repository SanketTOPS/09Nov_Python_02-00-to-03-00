from django.contrib import admin
from django.urls import path,include
from apiapp import views


urlpatterns = [
    path('getdata/',views.getdata),
    path('searchdata/<int:id>',views.searchdata),
    path('deletedata/<int:id>',views.deletedata),
]