# Generated by Django 3.2.9 on 2022-03-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20220228_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(blank=True, choices=[('1_year', '1 Year Program'), ('2_year', '2 Year Program')], max_length=100, null=True),
        ),
    ]
