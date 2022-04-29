# Generated by Django 3.2.9 on 2022-03-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions_bank',
            old_name='question_correct_option',
            new_name='correct_option',
        ),
        migrations.AddField(
            model_name='questions_bank',
            name='solution_image',
            field=models.ImageField(blank=True, null=True, upload_to='solution_images'),
        ),
        migrations.AddField(
            model_name='questions_bank',
            name='solution_text',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]