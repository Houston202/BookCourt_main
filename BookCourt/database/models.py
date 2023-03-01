from django.db import models


class Books(models.Model):
    Name = models.CharField('Название', max_length=250)
    Author = models.CharField('Автор', max_length=100)
    Description = models.TextField('Описание', max_length=10000)
    Price = models.IntegerField('Цена')
    Remainder = models.IntegerField('В наличии')
    Image = models.CharField('Картинка', max_length=1000)
    NumberOfPages = models.IntegerField('Количество страниц')
    Genre = models.CharField('Жанр', max_length=100)


    def __str__(self):
        return self.Name
