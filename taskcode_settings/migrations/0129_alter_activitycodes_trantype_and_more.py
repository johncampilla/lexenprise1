# Generated by Django 4.2.6 on 2024-07-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0128_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('PCT Filing Date', 'PCT Filing Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Registration Date', 'RegistrationDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Document Date', 'Document Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Priority Date', 'Priority Date'), ('IR Date', 'IR Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Publication Date', 'PublicationDate'), ('RunDate', 'RunDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Date Receipt', 'tran_date'), ('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date')], max_length=30, null=True),
        ),
    ]