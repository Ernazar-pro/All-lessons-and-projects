# Generated by Django 4.2.3 on 2023-08-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0003_rename_date_product_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_joined',
            field=models.DateField(),
        ),
    ]
