# Generated by Django 4.2.6 on 2024-07-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0106_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('OA Mailing Date', 'OA Mailing Date'), ('IR Date', 'IR Date'), ('PCT Publication Date', 'PCT Publication Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Renewal Date', 'Renewal Date'), ('Priority Date', 'Priority Date'), ('RunDate', 'RunDate'), ('Document Date', 'Document Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Registration Date', 'RegistrationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Publication Date', 'PublicationDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
    ]