# Generated by Django 3.1 on 2020-11-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0039_auto_20201118_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profilepic.jpg', null=True, upload_to=''),
        ),
    ]
