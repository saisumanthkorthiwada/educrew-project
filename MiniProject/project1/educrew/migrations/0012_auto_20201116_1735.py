# Generated by Django 3.1 on 2020-11-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0011_auto_20201113_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectinfo',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerschedule',
            name='p1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerschedule',
            name='p2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerschedule',
            name='p3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerschedule',
            name='p4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p4',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
