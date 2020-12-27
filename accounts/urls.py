from django.urls import path, include
from .views import RegisterUser, LogoutApiView, JWTUserLoginView

"""Url patters for, register to create new account, login and logout accounts"""
urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('login/', JWTUserLoginView.as_view()),
]