# Generated by Django 4.2.6 on 2024-03-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_bills_peso_rate_used_filingfees_peso_rate_used_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempope',
            name='PhPamount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tempope',
            name='USDamount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
