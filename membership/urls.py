from django.contrib import admin
from django.urls import path, include
from .views import helloAPI, userList, getUser, getRank, memberCreate, login, point

# μμ κ·μΉ
urlpatterns = [
    path('rank/',getRank),
    path('hello/',helloAPI),
    path('users/',userList),
    path('signin/',login),
    path('point/',point),
    path('users/signup/',memberCreate),
    path('<str:id>/',getUser),
    
]
