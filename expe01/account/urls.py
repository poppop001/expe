from django.urls import path

from account.views import hello

urlpatterns = [
    path('hello/',hello,name='hello')
]