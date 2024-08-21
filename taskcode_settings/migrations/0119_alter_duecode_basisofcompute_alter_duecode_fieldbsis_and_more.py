# Generated by Django 4.2.6 on 2024-07-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0118_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('Application Date', 'Application Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('Publication Date', 'PublicationDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Priority Date', 'Priority Date'), ('Registration Date', 'RegistrationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Receipt Date', 'Document Receipt Date'), ('IR Date', 'IR Date'), ('Renewal Date', 'Renewal Date'), ('PCT Filing Date', 'PCT Filing Date'), ('RunDate', 'RunDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date'), ('Date Receipt', 'tran_date')], max_length=30, null=True),
        ),
    ]
