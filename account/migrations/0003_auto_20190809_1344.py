# Generated by Django 2.2.1 on 2019-08-09 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studij', '0001_initial'),
        ('account', '0002_auto_20190809_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moj_Kolegij',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('kolegij_id', models.CharField(max_length=10)),
                ('studij_id', models.ForeignKey(default='pss', on_delete=django.db.models.deletion.CASCADE, to='studij.Studij')),
            ],
        ),
        migrations.DeleteModel(
            name='Student_Kolegij',
        ),
    ]
