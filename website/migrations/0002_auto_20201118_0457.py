# Generated by Django 3.0.7 on 2020-11-18 04:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 4, 57, 30, 235888, tzinfo=utc)),
        ),
    ]
