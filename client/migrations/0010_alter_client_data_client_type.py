# Generated by Django 4.2.6 on 2024-05-31 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_client_data_updatedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_data',
            name='client_type',
            field=models.CharField(blank=True, choices=[('Foreign', 'Foreign'), ('Local', 'Local')], max_length=10, null=True),
        ),
    ]
