# Generated by Django 3.2.9 on 2022-04-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20220403_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referal_code',
            name='qr_code_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]