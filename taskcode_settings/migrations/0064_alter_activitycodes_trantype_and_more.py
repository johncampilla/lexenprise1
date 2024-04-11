# Generated by Django 4.2.6 on 2024-03-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0063_alter_activitycodes_trantype_alter_duecode_fieldbsis'),
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
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date'), ('RunDate', 'RunDate'), ('IR Date', 'IR Date'), ('Publication Date', 'PublicationDate'), ('Document Date', 'Document Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Renewal Date', 'Renewal Date'), ('Registration Date', 'RegistrationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Priority Date', 'Priority Date')], max_length=30, null=True),
        ),
    ]