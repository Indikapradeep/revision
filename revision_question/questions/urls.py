from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name='questions'),
    path('grades/', views.grades, name='grades'),
    path('grade6subjects/', views.grade6subjects, name='grade6subjects'),
    path('grade11subjects/', views.grade11subjects, name='grade11subjects'),
    path('grade6maths/', views.grade6maths, name='grade6maths'),
    path('m6circlequestions/', views.m6circlequestions, name='m6circlequestions')
]