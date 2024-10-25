# Generated by Django 4.2.6 on 2024-10-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0145_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duecode',
            options={'verbose_name_plural': 'Due Codes'},
        ),
        migrations.AlterModelOptions(
            name='filingfeecodes',
            options={'verbose_name_plural': 'Filing Fee Codes'},
        ),
        migrations.AlterModelOptions(
            name='tasktemplates',
            options={'verbose_name_plural': 'Standard Templates'},
        ),
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
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Renewal Date', 'Renewal Date'), ('Registration Date', 'RegistrationDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Document Date', 'Document Date'), ('Document Receipt Date', 'Document Receipt Date'), ('IR Date', 'IR Date'), ('RunDate', 'RunDate'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Application Date', 'Application Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Priority Date', 'Priority Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Date Receipt', 'tran_date'), ('Document Date', 'doc_date'), ('Mailing Date', 'mailing_date')], max_length=30, null=True),
        ),
    ]
