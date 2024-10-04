# Generated by Django 4.2.6 on 2024-08-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0143_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('PCT Filing Date', 'PCT Filing Date'), ('RunDate', 'RunDate'), ('Document Receipt Date', 'Document Receipt Date'), ('Priority Date', 'Priority Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Publication Date', 'PublicationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Application Date', 'Application Date'), ('IR Date', 'IR Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Date', 'Document Date'), ('Renewal Date', 'Renewal Date'), ('Registration Date', 'RegistrationDate'), ('IR_subsequentDate', 'IR_subsequentDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date'), ('Date Receipt', 'tran_date')], max_length=30, null=True),
        ),
    ]