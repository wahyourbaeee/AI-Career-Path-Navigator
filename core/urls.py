from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('analyze/', views.analyze, name='analyze'),
]