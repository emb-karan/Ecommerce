# Generated by Django 3.1.3 on 2021-10-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211011_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='isactive',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cart',
            name='process_status',
            field=models.IntegerField(default=1),
        ),
    ]
