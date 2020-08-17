from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gtd-home'),
    path('about/', views.about, name='gtd-about'),
]