# Generated by Django 3.1.3 on 2021-10-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211011_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
