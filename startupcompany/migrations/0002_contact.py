# Generated by Django 4.0.5 on 2022-06-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupcompany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('subject', models.TextField()),
            ],
        ),
    ]