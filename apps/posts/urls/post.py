from django.urls import path, include
from posts.views import register_post, change_post, detail_post, delete_post, user_posts

urlpatterns = [
    # POSTS
    path('post/', include([
        path('register/', register_post, name='register_post'),
        
        path('<int:id_user>/', include([
            path('posts/user/', user_posts, name = "user_posts"),
        ])),

        path('post/<slug:slug_post>/', include([
            path('change/', change_post, name = "change_post"),
            path('detail/', detail_post, name = "detail_post"),
            path('delete/', delete_post, name = "delete_post"),
        ])),
    ])),
]