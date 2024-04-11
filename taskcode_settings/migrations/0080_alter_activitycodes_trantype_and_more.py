# Generated by Django 4.2.6 on 2024-03-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0079_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
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
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Years', 'In Years'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Priority Date', 'Priority Date'), ('Registration Date', 'RegistrationDate'), ('RunDate', 'RunDate'), ('Publication Date', 'PublicationDate'), ('OA Mailing Date', 'OA Mailing Date'), ('IR Date', 'IR Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Document Date', 'Document Date'), ('Renewal Date', 'Renewal Date')], max_length=30, null=True),
        ),
    ]
