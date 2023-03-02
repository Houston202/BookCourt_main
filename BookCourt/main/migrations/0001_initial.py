# Generated by Django 4.1.7 on 2023-03-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('mobile_phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Эмэйл')),
                ('url', models.CharField(max_length=150, verbose_name='Ссылка на сайт')),
                ('adres', models.CharField(max_length=150, verbose_name='Адрес')),
                ('name_of_major', models.CharField(max_length=150, verbose_name='Представитель (ФИО)')),
                ('password', models.CharField(max_length=150, verbose_name='Пароль')),
            ],
        ),
    ]
