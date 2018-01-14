from django.db import models

class Article(models.Model):
    articleName = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.articleName