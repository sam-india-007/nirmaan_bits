# Generated by Django 3.1.7 on 2021-03-28 17:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210307_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 17, 50, 20, 445063, tzinfo=utc)),
        ),
    ]