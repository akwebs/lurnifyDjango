# Generated by Django 3.2.9 on 2022-04-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20220415_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_and_study',
            name='crowns',
            field=models.IntegerField(default=1),
        ),
    ]
