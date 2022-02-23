from django.urls import path
from .views import *

urlpatterns = [
    #BLOG
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]