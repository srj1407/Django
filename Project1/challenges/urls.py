from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('<int:month>/', views.challenge_by_no),
    path('<str:month>/', views.challenge, name='month-challenge'),
]