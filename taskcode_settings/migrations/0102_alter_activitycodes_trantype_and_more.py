# Generated by Django 4.2.6 on 2024-04-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0101_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('IR Date', 'IR Date'), ('Registration Date', 'RegistrationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Document Receipt Date', 'Document Receipt Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('RunDate', 'RunDate'), ('OA Mailing Date', 'OA Mailing Date'), ('Priority Date', 'Priority Date'), ('Renewal Date', 'Renewal Date'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date'), ('Date Receipt', 'tran_date')], max_length=30, null=True),
        ),
    ]
