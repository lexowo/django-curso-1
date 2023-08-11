from django.urls import path
from . import views

urlpatterns=[
    path('', views.index), #dominio principal
    path('about/', views.about),
    path('hello/<str:username>', views.hello), #(params) entre morelessthan es solo una variable no algo especifico
    path('projects/', views.projects),
    path('tasks/<str:title>', views.tasks),
]