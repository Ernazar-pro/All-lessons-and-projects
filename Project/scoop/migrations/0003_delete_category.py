# Generated by Django 4.2.3 on 2023-08-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0002_category_alter_product_options_alter_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
