# Generated by Django 4.0.5 on 2022-06-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startupcompany', '0018_remove_apply_job_sex_alter_apply_job_experienc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply_job',
            old_name='experienc',
            new_name='pozition',
        ),
    ]
