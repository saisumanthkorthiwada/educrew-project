# Generated by Django 3.1 on 2020-11-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0013_auto_20201116_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentschedule',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
