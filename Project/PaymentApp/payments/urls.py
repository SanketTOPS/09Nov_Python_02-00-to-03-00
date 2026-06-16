from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_page, name='payment_page'),
    path('create_order/', views.create_order, name='create_order'),
    path('verify_payment/', views.verify_payment, name='verify_payment'),
]
