# Generated by Django 4.2.6 on 2024-03-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_bills_hourlyrate_bills_lawyer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempbills',
            name='USDamount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
