# Generated by Django 3.2.9 on 2022-03-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0003_auto_20220314_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_test',
            name='test_level',
            field=models.CharField(choices=[('1', 'level-1'), ('2', 'level-2'), ('3', 'level-3'), ('4', 'level-4')], default='1', max_length=10),
        ),
    ]
