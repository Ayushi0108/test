# Generated by Django 3.1.2 on 2020-11-25 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20201125_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 25, 11, 25, 33, 3512, tzinfo=utc)),
        ),
    ]
