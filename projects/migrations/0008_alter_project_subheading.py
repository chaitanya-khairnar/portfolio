# Generated by Django 3.2 on 2021-08-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_subheading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='subheading',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
