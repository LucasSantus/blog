from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name="Author",
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Title",
    )
    subtitle = models.CharField(
        max_length=200,
        null=True,
        verbose_name="SubTitle",
    )
    text = models.TextField(
        verbose_name="Text",
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Created Date",
    )
    published_date = models.DateTimeField(
        blank=True, 
        null=True,
        verbose_name="Published Date",
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title