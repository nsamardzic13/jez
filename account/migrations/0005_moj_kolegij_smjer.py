# Generated by Django 2.2.1 on 2019-09-11 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studij', '0004_auto_20190911_0819'),
        ('account', '0004_auto_20190911_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='moj_kolegij',
            name='smjer',
            field=models.ForeignKey(default='sm', on_delete=django.db.models.deletion.CASCADE, to='studij.Smjer'),
        ),
    ]
