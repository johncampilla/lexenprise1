# Generated by Django 4.2.6 on 2024-07-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0134_alter_activitycodes_trantype_alter_duecode_fieldbsis'),
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
            field=models.CharField(blank=True, choices=[('PCT Publication Date', 'PCT Publication Date'), ('Renewal Date', 'Renewal Date'), ('IR Date', 'IR Date'), ('PCT Filing Date', 'PCT Filing Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('RunDate', 'RunDate'), ('Priority Date', 'Priority Date'), ('Registration Date', 'RegistrationDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Application Date', 'Application Date'), ('Document Receipt Date', 'Document Receipt Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Years', 'In Years'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Date Receipt', 'tran_date'), ('Document Date', 'doc_date')], max_length=30, null=True),
        ),
    ]
