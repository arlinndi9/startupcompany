# Generated by Django 4.0.5 on 2022-06-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupcompany', '0013_alter_apply_job_experienc'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='position_requirement',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
