from django.urls import path
from . import views

urlpatterns = [
    #when first param is empty, we are creating a url path for the root page
    # if want to build on the url you would input '/download' as an example for the first param
    # 2nd param is a funtion called index you are importing used to render the html page. imported from the views.py file. Whatever index produces will be rendered to the user
    # 3rd param name gives the url path a name - usually the same as the function that is being imported from the views file
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]