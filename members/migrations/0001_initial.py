# Generated by Django 3.2.9 on 2022-03-31 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lurnify_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lurnify Member',
                'verbose_name_plural': 'Lurnify Members',
            },
        ),
        migrations.CreateModel(
            name='member_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Lurnify Member Types',
                'verbose_name_plural': 'Lur nify Member Types',
            },
        ),
        migrations.CreateModel(
            name='referal_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lurnify_member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.lurnify_member')),
            ],
        ),
        migrations.AddField(
            model_name='lurnify_member',
            name='member_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.member_type'),
        ),
        migrations.CreateModel(
            name='Bank_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lurnify_member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.lurnify_member')),
            ],
            options={
                'verbose_name': 'Lurnify Member',
                'verbose_name_plural': 'Lurnify Member Bank Details',
                'unique_together': {('lurnify_member_id', 'bank_name', 'branch_name', 'ifsc_code', 'account_no')},
            },
        ),
    ]
