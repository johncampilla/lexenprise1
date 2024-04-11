# Generated by Django 4.2.6 on 2024-03-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_alter_tempbills_usdamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='filingfees',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='ope',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='tempbills',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='tempfilingfees',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='tempope',
            name='peso_rate_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='tempbills',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Proforma', 'Proforma'), ('Billed', 'Billed'), ('Cancelled', 'Cancelled')], default='Open', max_length=15),
        ),
        migrations.AlterField(
            model_name='tempfilingfees',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Proforma', 'Proforma'), ('Billed', 'Billed'), ('Cancelled', 'Cancelled')], default='Open', max_length=15),
        ),
        migrations.AlterField(
            model_name='tempope',
            name='status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Proforma', 'Proforma'), ('Billed', 'Billed'), ('Cancelled', 'Cancelled')], default='Open', max_length=15),
        ),
    ]
