from django.urls import path
from . import views

urlpatterns=[
    path('', views.hello), #dominio principal
    path('about/', views.about)
]