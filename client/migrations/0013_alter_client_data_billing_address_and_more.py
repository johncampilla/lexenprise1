# Generated by Django 4.2.6 on 2024-07-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_alter_natureofbusiness_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_data',
            name='billing_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='billing_attention',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='billing_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='position',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='referredby',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]