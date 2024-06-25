# Generated by Django 5.0.6 on 2024-06-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=100)),
                ('role', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
