# Generated by Django 3.2 on 2021-04-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210422_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
