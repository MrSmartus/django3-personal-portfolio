from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) #вказуємо макс довжину заголовку
    description = models.CharField(max_length=250) #вказуємо макс.довжину опису
    image = models.ImageField(upload_to='portfolio/images/') #вказуємо папку, звідки будуть братись зображення
    url = models.URLField(blank=True) #відкривати посилання в новій вкладці

    def __str__(self):
        return self.title
