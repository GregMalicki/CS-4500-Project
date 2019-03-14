from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('delete/', views.delete),
    path('update/', views.update),
]
