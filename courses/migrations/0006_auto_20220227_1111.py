# Generated by Django 3.2.9 on 2022-02-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_dates_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='course_id',
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='courses.subjects'),
        ),
    ]
