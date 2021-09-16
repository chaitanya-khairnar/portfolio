# Generated by Django 3.2 on 2021-08-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='General_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]