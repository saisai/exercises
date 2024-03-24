from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name 


class Article(models.Model):
    headline = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    primary_categories = models.ManyToManyField(Category, related_name="primary_article_set")
    secondary_categories = models.ManyToManyField(Category, related_name="secondary_article_set")


    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return self.headline

