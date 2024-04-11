# Generated by Django 4.2.6 on 2024-03-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0098_alter_duecode_basisofcompute_alter_duecode_fieldbsis_and_more'),
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
            field=models.CharField(blank=True, choices=[('PCT Filing Date', 'PCT Filing Date'), ('RunDate', 'RunDate'), ('Registration Date', 'RegistrationDate'), ('IR Date', 'IR Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Renewal Date', 'Renewal Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Priority Date', 'Priority Date'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Date Receipt', 'tran_date'), ('Document Date', 'doc_date')], max_length=30, null=True),
        ),
    ]
