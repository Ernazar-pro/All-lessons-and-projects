# Generated by Django 4.2.3 on 2023-08-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0010_alter_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
