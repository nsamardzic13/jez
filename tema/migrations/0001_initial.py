# Generated by Django 2.2.1 on 2019-09-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('tema_id', models.AutoField(primary_key=True, serialize=False)),
                ('tema_ime', models.CharField(max_length=50)),
                ('kolegij_id', models.CharField(max_length=10)),
            ],
        ),
    ]
