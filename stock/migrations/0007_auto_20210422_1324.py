# Generated by Django 3.2 on 2021-04-22 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20210422_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='book',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='quantity',
            old_name='stock',
            new_name='stock_id',
        ),
    ]
