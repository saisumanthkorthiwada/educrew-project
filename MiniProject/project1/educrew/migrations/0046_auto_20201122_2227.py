# Generated by Django 3.1 on 2020-11-22 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0045_facultyachievement_studentachievement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='announcements',
            name='strt_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
