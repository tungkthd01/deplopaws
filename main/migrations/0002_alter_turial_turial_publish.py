# Generated by Django 3.2.8 on 2021-10-26 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turial',
            name='turial_publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 16, 2, 58, 258990), verbose_name='date publisher'),
        ),
    ]
