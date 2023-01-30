from django.urls import path

from myApp.views import personal_views,question_views,main_views

urlpatterns = [

    path('', main_views.hello_page),
    path('login/', personal_views.login),
    path('register/',personal_views.register),
    path('query/qlist',question_views.get_qlist),
    path('test',views.test),

]
