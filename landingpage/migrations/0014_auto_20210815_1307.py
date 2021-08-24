# Generated by Django 3.1.2 on 2021-08-15 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0013_auto_20210815_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='null', help_text='Enter you blog text here.', max_length=2000),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Lurnify', max_length=255),
        ),
    ]