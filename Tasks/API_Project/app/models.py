from django.db import models

class Author(models.Model):
    name = models.CharField('Имя', max_length=255)

    def __srt__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Book(models.Model):
    name = models.CharField('Имя книги', max_length=255)
    description = models.TextField('Описание')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'