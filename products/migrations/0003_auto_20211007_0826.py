# Generated by Django 3.2.7 on 2021-10-07 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211007_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='colletion',
            new_name='collection',
        ),
        migrations.AlterModelTable(
            name='collection',
            table='collections',
        ),
    ]
