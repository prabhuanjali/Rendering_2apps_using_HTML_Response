from django.urls import path
from app1.views import *

app_name='anything'

urlpatterns = [
    path('first/', first, name='first'),
    path('second/', second, name='second')
]