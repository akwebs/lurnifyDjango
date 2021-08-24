# Generated by Django 3.2.6 on 2021-08-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_rename_contact_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='createdAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]