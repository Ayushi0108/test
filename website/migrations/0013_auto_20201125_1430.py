# Generated by Django 3.1.2 on 2020-11-25 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20201125_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 25, 9, 0, 40, 838702, tzinfo=utc)),
        ),
    ]