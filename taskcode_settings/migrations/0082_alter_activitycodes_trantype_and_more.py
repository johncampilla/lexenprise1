# Generated by Django 4.2.6 on 2024-03-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0081_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Publication Date', 'PublicationDate'), ('Priority Date', 'Priority Date'), ('Document Date', 'Document Date'), ('Registration Date', 'RegistrationDate'), ('Renewal Date', 'Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date'), ('IR Date', 'IR Date'), ('PCT Filing Date', 'PCT Filing Date'), ('IR Renewal Date', 'IR Renewal Date'), ('RunDate', 'RunDate')], max_length=30, null=True),
        ),
    ]