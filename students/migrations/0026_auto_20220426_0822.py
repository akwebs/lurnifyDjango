# Generated by Django 3.2.9 on 2022-04-26 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_section', '0006_lurnifighter_referral'),
        ('students', '0025_auto_20220426_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral_and_winner',
            name='lurnifighter_referral_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_section.lurnifighter_referral'),
        ),
        migrations.DeleteModel(
            name='lurnifighter_referral',
        ),
    ]
