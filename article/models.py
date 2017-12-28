from django.db import models
from loginsys.models import Profile

class ArticleGroup(models.Model):
    class Meta:
        db_table = 'article_group'
    name = models.CharField(max_length=100)

class Article(models.Model):
    class Meta:
        db_table = 'article'
    title = models.CharField(max_length=200)
    text = models.TextField()
    article_group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
