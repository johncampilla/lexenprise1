# Generated by Django 4.2.6 on 2024-03-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0070_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Years', 'In Years'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Date', 'Document Date'), ('Renewal Date', 'Renewal Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Registration Date', 'RegistrationDate'), ('IR Date', 'IR Date'), ('OA Mailing Date', 'OA Mailing Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('RunDate', 'RunDate'), ('Priority Date', 'Priority Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Publication Date', 'PublicationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Application Date', 'Application Date')], max_length=30, null=True),
        ),
    ]
