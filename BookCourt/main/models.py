from django.db import models

class Users(models.Model):
    company_name = models.CharField('Название компании', max_length=100)
    mobile_phone = models.CharField('Телефон', max_length=15)
    email = models.CharField('Эмэйл', max_length=100)
    url = models.CharField('Ссылка на сайт', max_length=150)
    adres = models.CharField('Адрес', max_length=150)
    name_of_major = models.CharField('Представитель (ФИО)', max_length=150)
    password = models.CharField('Пароль', max_length=150)

    def __str__(self):
        return self.company_name
