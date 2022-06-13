from django.db import models
import random, string
from autoslug import AutoSlugField

class Base(models.Model):
    is_active = models.BooleanField(verbose_name = "Ativo", default = True)
    create_at = models.DateTimeField(verbose_name = "Data & Hora registrado", auto_now_add = True)
    update_at = models.DateTimeField(verbose_name = "Data & Hora modificado", auto_now_add = False, auto_now = True, blank = True, null = True)
    deactivate_at = models.DateTimeField(verbose_name = "Data & Hora desativado", auto_now_add = False, auto_now = True, blank = True, null = True)

    class Meta:
        abstract = True

    def get_generated_text_slug():
        return ''.join(random.choice(letters) for i in range(6))

class BaseAttributes(Base):
    title = models.CharField(verbose_name = "Título", max_length = 300, unique = True)
    slug = AutoSlugField(populate_from = 'title', unique_with = ['title'], unique = True, editable = True)

    class Meta:
        abstract = True