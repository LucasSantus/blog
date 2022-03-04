from django.urls import path, include
from .views import *

urlpatterns = [
    # BLOG
    path('post/<slug:slug_category>/register/', register_post, name='register_post'),
    path('post/<slug:slug_post>/', include([
        path('modify/', modify_post, name = "modify_post"),
        path('delete/', delete_post, name = "delete_post"),
        path('detail/', detail_post, name = "detail_post"),
    ])),

    # CATEGORY
    path('category/register/', register_category, name='register_category'),
    path('category/<slug:slug_category>/', include([
        path('modify/', modify_category, name = "modify_category"),
        path('delete/', delete_category, name = "delete_category"),
        path('detail/', detail_category, name = "detail_category"),
        path('view/', view_posts_category, name = "view_posts_category"),
    ])),
]