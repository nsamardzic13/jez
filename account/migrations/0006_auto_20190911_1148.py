# Generated by Django 2.2.1 on 2019-09-11 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_moj_kolegij_smjer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moj_kolegij',
            name='smjer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studij.Smjer'),
        ),
    ]
