# Generated by Django 3.2.7 on 2022-02-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(blank=True, choices=[('1_year', '1 Year Programe'), ('2_year', '2 Year Programe')], max_length=100, null=True),
        ),
    ]
