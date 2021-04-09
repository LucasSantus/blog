from django.urls import path
from .views import *

urlpatterns = [
    #EDITAR
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    
    #DETALHE
    path('post/<int:pk>/', post_detail, name='post_detail'),
]