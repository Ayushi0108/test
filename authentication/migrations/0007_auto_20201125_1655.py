# Generated by Django 3.1.2 on 2020-11-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_payment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
