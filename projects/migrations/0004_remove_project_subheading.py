# Generated by Django 3.2 on 2021-08-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210829_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='subheading',
        ),
    ]