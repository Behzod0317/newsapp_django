from distutils.command.upload import upload
from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField("Yangilik bo'limi", max_length=200)

    # more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class News(models.Model):
    name = models.CharField("News title", max_length=150)
    text = models.TextField("text")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="news")
    image = models.ImageField("Yangilik rasmi", upload_to="image")


    # more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

