# Generated by Django 3.2 on 2021-04-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20210422_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='quantity',
            old_name='stock_id',
            new_name='stock',
        ),
    ]
