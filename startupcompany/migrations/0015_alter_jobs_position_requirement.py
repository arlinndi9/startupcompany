# Generated by Django 4.0.5 on 2022-06-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupcompany', '0014_jobs_position_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='position_requirement',
            field=models.CharField(max_length=255),
        ),
    ]
