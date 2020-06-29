from django.urls import path
from portapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
]
