# Generated by Django 4.2.6 on 2024-03-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0096_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('Renewal Date', 'Renewal Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Publication Date', 'PublicationDate'), ('IR Date', 'IR Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Priority Date', 'Priority Date'), ('RunDate', 'RunDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('OA Mailing Date', 'OA Mailing Date'), ('Registration Date', 'RegistrationDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Mailing Date', 'mailing_date'), ('Document Date', 'doc_date'), ('Date Receipt', 'tran_date')], max_length=30, null=True),
        ),
    ]
