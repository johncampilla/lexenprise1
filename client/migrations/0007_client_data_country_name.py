# Generated by Django 4.2.6 on 2024-03-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_remove_client_data_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_data',
            name='country_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
