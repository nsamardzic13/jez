# Generated by Django 2.2.1 on 2019-07-27 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_student_email_ver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studij_id',
        ),
    ]
