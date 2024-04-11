# Generated by Django 4.2.6 on 2024-02-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0053_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Renewal Date', 'Renewal Date'), ('IR Date', 'IR Date'), ('RunDate', 'RunDate'), ('Document Receipt Date', 'Document Receipt Date'), ('Registration Date', 'RegistrationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Application Date', 'Application Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Publication Date', 'PublicationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Priority Date', 'Priority Date'), ('Document Date', 'Document Date'), ('PCT Publication Date', 'PCT Publication Date')], max_length=30, null=True),
        ),
    ]