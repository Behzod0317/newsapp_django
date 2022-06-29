from django.db import models


class News(models.Model):
    name = models.CharField("Yangilik nomi", max_length=150)
    text = models.TextField("Yangilik matni")

    # more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

