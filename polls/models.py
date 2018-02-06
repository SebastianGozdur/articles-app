from django.db import models

class Article(models.Model):
    articleName = models.CharField(max_length=100)
    fileName = models.CharField(max_length=100)
    rating = models.IntegerField()
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.articleName