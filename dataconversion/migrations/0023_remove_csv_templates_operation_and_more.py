# Generated by Django 4.2.6 on 2024-07-23 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0022_csv_templates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_templates',
            name='Operation',
        ),
        migrations.RemoveField(
            model_name='csv_templates',
            name='TaskCode',
        ),
        migrations.RemoveField(
            model_name='csv_templates',
            name='WithEnclosure',
        ),
    ]
