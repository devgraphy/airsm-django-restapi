from django.contrib import admin
from django.urls import path, include
from .views import helloAPI, userList, getUser, getRank,signIn

# 순서 규칙
urlpatterns = [
    path('rank/',getRank),
    path('hello/',helloAPI),
    path('users/',userList),
    path('signin/',signIn),
    path('<str:id>/',getUser),
]
