# Generated by Django 3.2.9 on 2022-04-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20220406_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lurnifighter_badges',
            options={'verbose_name': 'Creates Lurnifighter Badges Levels', 'verbose_name_plural': 'Creates Lurnifighter Badges Levels'},
        ),
        migrations.AlterModelOptions(
            name='lurnifighter_referral',
            options={'verbose_name': 'Creates Lurnifighter Referral Badges', 'verbose_name_plural': 'Creates Lurnifighter Referral Badges'},
        ),
        migrations.RemoveField(
            model_name='lurnifighter_levels',
            name='challenge_completed',
        ),
        migrations.RemoveField(
            model_name='lurnifighter_levels',
            name='level_end_date',
        ),
        migrations.RemoveField(
            model_name='lurnifighter_levels',
            name='level_start_date',
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='refer_freinds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='study_effectiveness',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='test_performances',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='total_crowns',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='total_study_hours',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='lurnifighter_levels',
            name='total_test',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]