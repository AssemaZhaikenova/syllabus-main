# Generated by Django 4.2.7 on 2023-11-10 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0002_remove_evaluationsystem_criteria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='user',
        ),
    ]
