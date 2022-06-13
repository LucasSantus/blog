from django.db import models
from home.models import BaseAttributes

class Post(BaseAttributes):
    subtitle = models.CharField(verbose_name = "Sub Título", unique = False, max_length = 120, null = True)
    resume = models.CharField(verbose_name = "Resumo", max_length = 130, blank = True, null = True)
    description = models.TextField(verbose_name = "Descrição", blank = True, null = True)

    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Author", related_name = "author_post_fk")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "post"
        app_label = "posts"

    def save(self, *args, **kwargs):
        self.resume = str(self.description[:120] + "...")
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title