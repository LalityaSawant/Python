from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('/task/', views.index, name="list"),
    path('/update_task/<str:pk>/', views.update_task, name="update_task"),
    path('/delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('/review_task/', views.review_task, name="review_task"),
]
