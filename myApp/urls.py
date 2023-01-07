from django.urls import path

from myApp import views

urlpatterns = [

    path('', views.main),
    path('login/', views.login),
    path('register/',views.register),
    path('init/',views.init)

]
