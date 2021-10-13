# Generated by Django 3.1.3 on 2021-10-12 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_auto_20211012_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now=True)),
                ('amt_status', models.CharField(max_length=200)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
