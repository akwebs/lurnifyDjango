# Generated by Django 3.2.9 on 2022-04-26 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_section', '0004_monthly_challange_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='lurnifighter_badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level_name', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lurnifighter Badges Levels',
                'verbose_name_plural': 'Lurnifighter Badges Levels',
            },
        ),
        migrations.CreateModel(
            name='weekly_challange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('week_name', models.CharField(max_length=50)),
                ('week_number', models.IntegerField(blank=True, null=True)),
                ('total_study_hours', models.FloatField(blank=True, null=True)),
                ('total_test', models.IntegerField(blank=True, default=0, null=True)),
                ('total_crowns', models.IntegerField(blank=True, default=0, null=True)),
                ('refer_freinds', models.IntegerField(blank=True, default=0, null=True)),
                ('test_performances', models.FloatField(blank=True, default=0, null=True)),
                ('study_effectiveness', models.IntegerField(blank=True, default=0, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('lurnifighter_badges_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_section.lurnifighter_badges')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Weekly Challenge',
                'verbose_name_plural': 'Weekly Challenge',
            },
        ),
        migrations.CreateModel(
            name='weekly_reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trophy', models.BooleanField(default=True)),
                ('no_of_coins', models.BigIntegerField(blank=True, default=0, null=True)),
                ('refer_freind_coupons', models.IntegerField(blank=True, default=0, null=True)),
                ('cash_coupons_id', models.ManyToManyField(blank=True, to='admin_section.cash_coupons')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('weekly_challange_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_section.weekly_challange')),
            ],
            options={
                'verbose_name': 'Weekly Reward',
                'verbose_name_plural': 'Weekly Reward',
            },
        ),
    ]