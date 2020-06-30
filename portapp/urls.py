from django.urls import path
from portapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('skills/', views.skills, name = 'skills'),
    path('resume/', views.resume, name = 'resume'),
    path('projects/', views.projects, name = 'projects'),
    path('certifications/', views.certifications, name = 'certifications'),
]
