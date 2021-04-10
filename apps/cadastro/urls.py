from django.urls import path
from .views import *

urlpatterns = [
    #CADASTRAR
    path('post/new/', post_new, name='post_new'),
]