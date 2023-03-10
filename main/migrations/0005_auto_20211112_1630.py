# Generated by Django 3.2.9 on 2021-11-12 09:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211112_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='up_load_file'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='main.usercreated'),
        ),
        migrations.AlterField(
            model_name='turial',
            name='turial_publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 30, 9, 567137), verbose_name='date publisher'),
        ),
    ]
