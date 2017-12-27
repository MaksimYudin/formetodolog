from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    class Meta:
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()

