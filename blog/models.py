from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('post_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def get_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'about'