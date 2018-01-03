from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
