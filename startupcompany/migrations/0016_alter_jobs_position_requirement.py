# Generated by Django 4.0.5 on 2022-06-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupcompany', '0015_alter_jobs_position_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='position_requirement',
            field=models.CharField(default='requiremts', max_length=255),
        ),
    ]