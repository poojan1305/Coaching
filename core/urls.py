from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('subjects/', views.subjects, name='subjects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
