# Generated by Django 3.1.3 on 2020-11-12 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0005_auto_20201112_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturerschedule',
            name='unq_id',
        ),
        migrations.RemoveField(
            model_name='studentschedule',
            name='unq_id',
        ),
    ]
