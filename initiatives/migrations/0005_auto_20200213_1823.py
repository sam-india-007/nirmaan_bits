# Generated by Django 2.2 on 2020-02-13 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0004_auto_20200213_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitiativeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_on', models.DateField(default=datetime.datetime(2020, 2, 13, 12, 53, 53, 866708, tzinfo=utc))),
                ('message', models.TextField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='initiative',
            name='date_started',
            field=models.DateField(default=datetime.datetime(2020, 2, 13, 12, 53, 53, 755534, tzinfo=utc), verbose_name='Start Date'),
        ),
        migrations.DeleteModel(
            name='InitiativeComments',
        ),
        migrations.AddField(
            model_name='initiativecomment',
            name='initiative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='initiatives.Initiative'),
        ),
    ]
