# Generated by Django 2.2.1 on 2019-07-27 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objava', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editobjave',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 11, 32, 29, 780170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='objava',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 27, 11, 32, 29, 780170, tzinfo=utc)),
        ),
    ]
