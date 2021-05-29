from django.contrib import admin
from django.urls import path, include
from .views import helloAPI, userList, getUser, getRank, memberCreate
from django.contrib.auth import views as auth_views

# 순서 규칙
urlpatterns = [
    path('rank/',getRank),
    path('hello/',helloAPI),
    path('users/',userList),
    path('signin/',auth_views.LoginView.as_view()),
    path('users/signup/',memberCreate),
    path('<str:id>/',getUser),
    
]
