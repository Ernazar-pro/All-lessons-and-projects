# Generated by Django 4.2.3 on 2023-08-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0004_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
