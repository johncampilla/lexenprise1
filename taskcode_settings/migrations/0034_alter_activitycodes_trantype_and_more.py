# Generated by Django 4.2.6 on 2024-01-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0033_alter_activitycodes_trantype_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('BILLABLE', 'BILLABLE'), ('MAILSIN', 'MAILSIN')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Years', 'In Years'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('PCT Filing Date', 'PCT Filing Date'), ('IR Date', 'IR Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Priority Date', 'Priority Date'), ('Renewal Date', 'Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('RunDate', 'RunDate'), ('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Registration Date', 'RegistrationDate'), ('Document Date', 'Document Date'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date')], max_length=30, null=True),
        ),
    ]