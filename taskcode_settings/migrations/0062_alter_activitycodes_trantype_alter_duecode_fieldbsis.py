# Generated by Django 4.2.6 on 2024-03-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0061_alter_activitycodes_trantype_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('IR Date', 'IR Date'), ('Document Receipt Date', 'Document Receipt Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Renewal Date', 'Renewal Date'), ('Publication Date', 'PublicationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('RunDate', 'RunDate'), ('Registration Date', 'RegistrationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('Priority Date', 'Priority Date'), ('Application Date', 'Application Date')], max_length=30, null=True),
        ),
    ]
