# Generated by Django 3.2.9 on 2022-04-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='academic_limits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_no', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Academic Update Limit',
                'verbose_name_plural': 'Academic Update Limits',
            },
        ),
    ]
