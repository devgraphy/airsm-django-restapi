from django.contrib import admin
from django.urls import path, include
from .views import userList, getUser
urlpatterns = [
    path('users/',userList),
    path('<str:phone>/',getUser)
]
