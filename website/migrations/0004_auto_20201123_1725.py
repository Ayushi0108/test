# Generated by Django 3.1.2 on 2020-11-23 11:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201118_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 11, 55, 0, 13867, tzinfo=utc)),
        ),
    ]
