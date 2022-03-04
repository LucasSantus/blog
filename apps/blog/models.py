from django.db import models
from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    title = models.CharField(verbose_name = "Título", max_length = 50)
    slug = AutoSlugField(populate_from = 'title', unique = True, editable = True, null = True, blank = True)
    time_registered = models.DateTimeField(verbose_name = "Data & Horário registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
        db_table = "category"
        app_label = "blog"

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, verbose_name="Author", related_name = "author_TutorialFK")
    category = models.ForeignKey(Category, related_name = "category_TutorialFK", on_delete = models.CASCADE)
    title = models.CharField(verbose_name = "Título", unique = True, max_length = 50)
    subtitle = models.CharField(verbose_name = "Sub Título", unique = False, max_length = 120, null = True)
    resume = models.CharField(verbose_name = "Resumo", max_length = 130, blank = True, null = True)
    description = models.TextField(verbose_name = "Descrição", blank = True, null = True)
    slug = AutoSlugField(populate_from = 'get_full_title', editable = True)
    time_registered = models.DateTimeField(verbose_name = "Data & Horário registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "post"
        app_label = "blog"

    def get_full_title(self):
        return str(self.title + " " + self.subtitle)

    def save(self, *args, **kwargs):
        self.resume = str(self.description[:120] + "...")
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title