from django.urls import path

from myApp import views

urlpatterns = [

    path('', views.main),
    path('login/', views.login),
    path('register/',views.register),
    path('init/',views.init),
    path('query/qlist',views.get_qlist),
    path('test',views.test)

]
