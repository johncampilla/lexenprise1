# Generated by Django 4.2.6 on 2024-03-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0056_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Registration Date', 'RegistrationDate'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Renewal Date', 'Renewal Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Priority Date', 'Priority Date'), ('PCT Filing Date', 'PCT Filing Date'), ('IR Date', 'IR Date'), ('OA Mailing Date', 'OA Mailing Date'), ('RunDate', 'RunDate'), ('Document Receipt Date', 'Document Receipt Date')], max_length=30, null=True),
        ),
    ]
