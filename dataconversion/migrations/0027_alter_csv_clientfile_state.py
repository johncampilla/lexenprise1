# Generated by Django 4.2.6 on 2024-07-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0026_csv_clientfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_clientfile',
            name='state',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
