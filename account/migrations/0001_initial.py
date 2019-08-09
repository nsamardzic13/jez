# Generated by Django 2.2.1 on 2019-08-09 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studij', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_ver', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(default='/profile_image/default.png', upload_to='profile_image')),
                ('studij_id', models.ForeignKey(default='pss', on_delete=django.db.models.deletion.CASCADE, to='studij.Studij')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Moji_Kolegiji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('kolegij_id', models.CharField(max_length=10)),
                ('studij_id', models.ForeignKey(default='pss', on_delete=django.db.models.deletion.CASCADE, to='studij.Studij')),
            ],
        ),
    ]
