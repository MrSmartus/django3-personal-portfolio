from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) #вказуємо макс довжину заголовку
    date = models.DateField()
    description = models.TextField() #вказуємо макс.довжину опису

    def __str__(self):
        return self.title
