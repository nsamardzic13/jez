# Generated by Django 2.2.3 on 2019-07-27 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studij',
            fields=[
                ('studij_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('studij_ime', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Kolegij',
            fields=[
                ('dummy_id', models.AutoField(primary_key=True, serialize=False)),
                ('kolegij_id', models.CharField(max_length=10)),
                ('kolegij_ime', models.CharField(max_length=60)),
                ('semestar', models.SmallIntegerField()),
                ('studij_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studij.Studij')),
            ],
        ),
    ]
