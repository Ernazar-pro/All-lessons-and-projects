from django.db import models

class Product(models.Model):
    name = models.CharField('Имя продукта', max_length=256)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена продукта')

    def __str__ (self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'