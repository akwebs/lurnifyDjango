# Generated by Django 3.2.7 on 2022-02-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
