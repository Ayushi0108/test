# Generated by Django 3.1.2 on 2020-11-25 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20201125_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 25, 19, 39, 26, 893565, tzinfo=utc)),
        ),
    ]