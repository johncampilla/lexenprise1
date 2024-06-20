# Generated by Django 4.2.6 on 2024-04-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0104_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Application Date', 'Application Date'), ('OA Mailing Date', 'OA Mailing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('RunDate', 'RunDate'), ('IR Date', 'IR Date'), ('Priority Date', 'Priority Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Publication Date', 'PublicationDate'), ('Registration Date', 'RegistrationDate'), ('Renewal Date', 'Renewal Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Document Date', 'Document Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Receipt Date', 'Document Receipt Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Date Receipt', 'tran_date'), ('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date')], max_length=30, null=True),
        ),
    ]