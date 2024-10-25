from django.db import models
from django.utils import timezone
import time


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Título')
    content = models.TextField(verbose_name='Conteúdo')
    author = models.ForeignKey('auth.user', on_delete=models.PROTECT, verbose_name='Autor',
                               related_name='posts', editable=False)
    number_views = models.IntegerField(default=0, verbose_name='Visualizações', editable=False)
    created_at = models.DateTimeField(verbose_name="Criado em", null=True, editable=False)
    tags = models.ManyToManyField('Tag', related_name='posts')


    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if not self.created_at:
            self.created_at = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=35, unique=True, verbose_name='Tag')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
