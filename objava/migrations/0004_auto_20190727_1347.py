# Generated by Django 2.2.1 on 2019-07-27 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objava', '0003_auto_20190727_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editobjave',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 11, 47, 36, 819089, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='objava',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 11, 47, 36, 819089, tzinfo=utc)),
        ),
    ]
