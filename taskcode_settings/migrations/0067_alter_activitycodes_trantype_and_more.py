# Generated by Django 4.2.6 on 2024-03-16 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0066_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('RunDate', 'RunDate'), ('Application Date', 'Application Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Priority Date', 'Priority Date'), ('PCT Filing Date', 'PCT Filing Date'), ('OA Mailing Date', 'OA Mailing Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Renewal Date', 'Renewal Date'), ('Publication Date', 'PublicationDate'), ('Document Date', 'Document Date'), ('Registration Date', 'RegistrationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('IR Date', 'IR Date')], max_length=30, null=True),
        ),
    ]
